<h4 align='center'>
  
![Logo](https://github.com/user-attachments/assets/8e784d01-0977-410a-ae11-7ebc30a08061)

</h4>

<h4 align='center'>
  
![Static Badge](https://img.shields.io/badge/version-1.0.0-red)
![Static Badge](https://img.shields.io/badge/bloome-fullstack_social_network-blue)
![Static Badge](https://img.shields.io/badge/python-django-green)
</h4>

<hr>
<h2 align='center'> Fullstack Django social media web app with newsfeed, chat, friends and so on. </h2>


<p>
This project is a FullStack Django based Social Network Website similar to Facebook •	Newsfeed, Chat system, Friend Request send and receive, Likes, Comments and so on.

  Technologies: Django, HTMX, Python, Bootstrap, CSS, JS, WebSocket, Django-Channel 

</p>

## Demo:

Live Website: https://bloome.pythonanywhere.com/
<br>
Mail: demo@gmail.com
<br>
Password: demo1234

## Demo Screenshots

<div class="image-container">
<p align='center'>
<img alt="demo" width="400" src="https://github.com/user-attachments/assets/680567a2-9bf2-4f3b-93a3-3b68ff28293e">
<img alt="demo" width="300" src="https://github.com/user-attachments/assets/e98c0639-400c-4f8b-ac9c-d63a18c712fb">
<hr>
<img alt="demo" width="400" src="https://github.com/user-attachments/assets/cf7435d6-3848-481e-b390-b1680fc608a3">
<img alt="demo" width="400" src="https://github.com/user-attachments/assets/3f79e369-b11e-40ac-bbd9-6820a803eff7">

</p>
</div>



## Locally Setup

Note: You can add both MySQL or SQLite database. The configuration is added in the settings.py so you just have to uncomment the code and set database host, user, password and port. 

Warning: If you face any database related error then you have to add the information by using python-dot-env or directly in the code of MySQL setup.

Clone the repository & Navigate to the project directory:

```bash
  git clone https://github.com/emhash/Bloome

  cd Bloome
```

Create a virtual envoirnment:

```bash 
python -m venv myenv
```
Active virtual envoirnment with Bash terminal:
```bash 
source myenv/Scripts/activate
```
(You can activate the virtual envoirnment using any terminal. Based on the terminal the activation process of virtual envoirnment might be different)

Now install the necessary module & start the server:
```bash 
pip install -r requirements.txt
python manage.py runserver

```
** In case of migration problem migrate and then run the server **
```bash 
python manage.py makemigrations
python manage.py migrate

```
## Tech Stack

**Front-End:** Html, CSS, Bootstrap, JavaScript

**Back-End:** Django, Sqlite or MySQL, Python, JS, HTMX


## Author

- [@emhash](https://www.github.com/emhash)


![App Screenshot]()

