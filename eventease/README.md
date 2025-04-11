
# 🎉 EventEase - Django Event Management System

EventEase is a feature-rich event management system built with Django and MySQL. It helps users seamlessly create, manage, RSVP, and share events with ease. Whether it’s a conference, workshop, or casual meetup – EventEase is your all-in-one planner.

---

## 🚀 Features

- ✅ User Registration & Login (with Profiles)
- ✅ Create, View, Edit, and Delete Events
- ✅ RSVP System (Yes/No response with timestamps)
- ✅ Upcoming Event Reminders Section
- ✅ Share Event:
  - 📋 Copy Message
  - 📤 WhatsApp Share
  - 📧 Send Email Invitations (with SMTP)
- ✅ Beautiful, responsive UI using Bootstrap
- ✅ User Profile: Phone & Bio fields (editable)

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap5
- **Database**: MySQL
- **Authentication**: Django Auth
- **Email Integration**: SMTP (Gmail)

---

## ⚙️ Setup Instructions

### 🔧 Requirements

- Python 3.8+
- MySQL Server
- pip / virtualenv (recommended)

### 🔨 Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/eventease.git
cd eventease

# 2. Create virtual environment & activate
python -m venv .venv
.venv\Scripts\activate  # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Import MySQL Schema
# Open MySQL Workbench or CLI and run:
# schema.sql from the project directory
```

### 🔧 Configure `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eventease_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Email setup for sending invitations
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'  # Use Gmail App Password
```

### ⚙️ Apply Migrations & Run Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Testing Credentials

Use the following credentials to test the app:

```
👤 Username: Sahana
🔑 Password: Dhruthi@2
```

---

## 🧠 Folder Structure

```
eventease/
│
├── eventease/           # Project settings
├── accounts/            # User management (Register/Login/Profile)
├── events/              # Event logic (CRUD, RSVP, reminders)
├── templates/           # All HTML files
├── static/              # CSS/JS files
├── schema.sql           # Database schema
├── README.md
└── manage.py
```

---

## 🤝 Collaboration & Contact

We welcome collaborators! Feel free to fork and submit PRs.

📩 **Get in Touch:**  
- Email: `sahanagn275@gmail.com`  
- LinkedIn: [linkedin.com/in/sahanagn](https://linkedin.com/in/sahanagn)  
- GitHub: [github.com/yourusername](https://github.com/yourusername)

---

## 📄 License

This project is licensed under the MIT License.

Happy coding! 🚀
