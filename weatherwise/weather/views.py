import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import FavoriteLocation
from .forms import RegisterForm
from datetime import datetime
from collections import defaultdict

API_KEY = "555926e6a165d8aa19497ca4801532c4"


# Home Page & Weather Search
def home(request):
    weather_data = None
    hourly_forecast = None
    daily_forecast = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")
        weather_data, hourly_forecast, daily_forecast, error = get_weather_and_forecast(city)  # ✅ Match the return values

    favorites = FavoriteLocation.objects.filter(user=request.user) if request.user.is_authenticated else []

    # Fetch weather for each favorite city
    updated_favorites = []
    for fav in favorites:
        fav_weather, _, _, _ = get_weather_and_forecast(fav.city)
        if fav_weather:
            updated_favorites.append({
                "city": fav.city,
                "temperature": fav_weather["temperature"],
                "description": fav_weather["description"],
                "humidity": fav_weather["humidity"],
                "wind_speed": fav_weather["wind_speed"],
                "wind_direction": fav_weather["wind_direction"],
            })

    favorite_cities = [fav.city for fav in favorites]

    return render(request, "weather/home.html", {
        "weather": weather_data,
        "hourly_forecast": hourly_forecast,
        "daily_forecast": daily_forecast,
        "error": error,
        "favorites": updated_favorites,
        "favorite_cities": favorite_cities
    })

# Register a new user
def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "weather/register.html", {"form": form})

# Login user
def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "weather/login.html", {"error": "Invalid credentials"})

    return render(request, "weather/login.html")

# Logout user
def logout_user(request):
    logout(request)
    return redirect("home")

# Save favorite location (only logged-in users)
@login_required
def save_favorite(request):
    if request.method == "POST":
        city = request.POST.get("city")
        if city and not FavoriteLocation.objects.filter(user=request.user, city=city).exists():
            FavoriteLocation.objects.create(user=request.user, city=city)
    return redirect("home")

# Delete favorite location
@login_required
def delete_favorite(request, city):
    FavoriteLocation.objects.filter(user=request.user, city=city).delete()
    return redirect("home")


def weather_by_city(request, city):
    weather_data, hourly_forecast, daily_forecast, error = get_weather_and_forecast(city)  # ✅ Fetch full forecast

    favorites = FavoriteLocation.objects.filter(user=request.user) if request.user.is_authenticated else []

    return render(request, "weather/home.html", {
        "weather": weather_data,
        "hourly_forecast": hourly_forecast,  # ✅ Fixed: Now it gets hourly forecast
        "daily_forecast": daily_forecast,    # ✅ Fixed: Now it gets 5-day forecast
        "error": error,
        "favorites": favorites
    })


# Fetch Weather & Forecast Data
def get_weather_and_forecast(city):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    weather_response = requests.get(weather_url).json()
    forecast_response = requests.get(forecast_url).json()

    weather_data = None
    hourly_forecast = None
    daily_forecast = None
    error = None

    if weather_response.get("cod") == 200:
        weather_data = {
            "city": weather_response["name"],
            "country": weather_response["sys"]["country"],
            "temperature": weather_response["main"]["temp"],
            "description": weather_response["weather"][0]["description"],
            "icon": weather_response["weather"][0]["icon"],
            "humidity": weather_response["main"]["humidity"],
            "wind_speed": weather_response["wind"]["speed"],
            "wind_direction": weather_response["wind"]["deg"]
        }
    else:
        error = "City not found!"

    if forecast_response.get("cod") == "200":
        hourly_forecast = []
        daily_data = defaultdict(list)  # Group forecasts by day

        for forecast in forecast_response["list"]:
            time_obj = datetime.strptime(forecast["dt_txt"], "%Y-%m-%d %H:%M:%S")
            formatted_time = time_obj.strftime("%I:%M %p")  # 12-hour format
            date_key = time_obj.strftime("%Y-%m-%d")  # Extract the date

            forecast_entry = {
                "time": formatted_time,
                "temp": forecast["main"]["temp"],
                "humidity": forecast["main"]["humidity"],
                "wind_speed": forecast["wind"]["speed"],
                "wind_direction": forecast["wind"]["deg"],
                "conditions": forecast["weather"][0]["description"],
                "icon": forecast["weather"][0]["icon"]
            }

            if len(hourly_forecast) < 8:  # Next 24 hours (3-hour intervals)
                hourly_forecast.append(forecast_entry)

            daily_data[date_key].append(forecast_entry)

        # Process 5-day forecast (taking the **midday data**)
        daily_forecast = []
        for date, forecasts in list(daily_data.items())[:5]:  # Take 5 days
            midday_index = len(forecasts) // 2  # Get middle forecast for the day
            daily_forecast.append({
                "date": datetime.strptime(date, "%Y-%m-%d").strftime("%A, %b %d"),  # Format: "Monday, Mar 25"
                "temp": forecasts[midday_index]["temp"],
                "humidity": forecasts[midday_index]["humidity"],
                "wind_speed": forecasts[midday_index]["wind_speed"],
                "wind_direction": forecasts[midday_index]["wind_direction"],
                "conditions": forecasts[midday_index]["conditions"],
                "icon": forecasts[midday_index]["icon"]
            })

    return weather_data, hourly_forecast, daily_forecast, error
