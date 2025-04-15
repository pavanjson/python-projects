# 📸 PhotoFusion - A Dynamic Photo Gallery Web App

**PhotoFusion** is a full-featured photo gallery web application where users can upload, organize, and manage their photos in albums with intuitive navigation, search, and customization. Built with Django, MySQL, and Bootstrap for a seamless modern user experience.

---

## 🚀 Features

- ✅ User Authentication (Login, Register, Profile Picture, Delete Account)
- ✅ Upload Photos to Albums
- ✅ Create New Albums on Upload
- ✅ Search Photos by Caption or Album
- ✅ Fullscreen Image Viewer with Prev/Next Navigation
- ✅ Paginated Photo Display
- ✅ Profile Avatar in Navbar with Edit/Delete Options
- ✅ Mobile-Responsive UI using Bootstrap 5

---

## 🛠 Tech Stack

| Frontend      | Backend       | Database  | Other            |
|---------------|---------------|-----------|------------------|
| HTML, CSS     | Django (Python)| MySQL     | Bootstrap 5, JS  |

---

## 🏁 Setup Instructions

### 1. 📦 Clone the Repository
```bash
git clone https://github.com/your-username/photofusion.git
cd photofusion
```

### 2. 🐍 Create Virtual Environment & Activate
```bash
python -m venv env
source env/bin/activate  # For Windows: env\\Scripts\\activate
```

### 3. 📥 Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. ⚙️ Configure Database

- Create a MySQL database named: `photofusion_db`
- Import schema from the file:

```bash
mysql -u root -p photofusion_db < schema.sql
```

- Update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'photofusion_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 5. 🔧 Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 🖼️ Create Static & Media Folders
```
/static/gallery/css/style.css
/static/gallery/js/script.js
/media/photos/
/media/avatars/
```

---

## 👤 Testing Credentials

| Username   | Password   | Role    |
|------------|------------|---------|
| `admin`    | `admin`    | Admin   |
| `testuser` | `testuser` | Regular |

---

## 🚦 Run the Project

```bash
python manage.py runserver
```

Open browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Folder Structure

```
photofusion/
├── gallery/                # Main app
│   ├── models.py           # Album, Photo, Profile
│   ├── views.py            # Views logic
│   ├── forms.py            # Forms (Photo, Profile)
│   ├── templates/gallery/  # HTML files
│   ├── static/gallery/     # CSS, JS
├── media/                  # Uploaded images & avatars
├── photofusion/            # Project settings
├── schema.sql              # MySQL table structure
├── requirements.txt
└── manage.py
```

---

## 💡 To Do / Future Enhancements

- Add album cover thumbnails
- Enable photo sharing links
- Social login (Google, GitHub)
- Dark mode toggle 🌙

---

## 📃 License

MIT License. © 2025 PhotoFusion by [Vinay SkyllX](mailto:vinay@skyllx.com) or [Vinay H P](mailto:vinayhp.paramesh@gmail.com).

---

**Built with ❤️ using Django & Bootstrap**