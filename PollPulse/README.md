# 🗳️ PollPulse

PollPulse is a dynamic online polling system built with Django that allows users to create polls, vote, and view results in real-time. It supports role-based dashboards, poll scheduling, image uploads, and a modern Bootstrap-powered UI.

---

## 📚 Project Overview

**PollPulse** enables users to:
- ✅ Create, edit, and delete polls with multiple options.
- ✅ Vote on live polls and see animated real-time results.
- ✅ Authenticate securely (Admin/User roles).
- ✅ Access custom dashboards based on user role.
- ✅ Schedule polls with start and end times.
- ✅ Attach images to polls for visual context.
- ✅ Receive OTP-based email verification during registration.
- ✅ Experience a modern, responsive design with feedback and alerts.

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Backend:** Django 5.1.7 (Python 3.11+)
- **Database:** MySQL

---

## 🚀 Key Features

### 🎯 Poll Management
- Create, update, delete, and manage polls.
- Set future poll schedule with `start_date` and `end_date`.
- Upload image banners for polls.
- Use modelformset with add/remove option support dynamically.
- Duplicate options are automatically restricted.
- Validation shown clearly with messages and field-level hints.

### 👥 Role-Based User Access
- **Admins**:
  - Full control over polls.
  - View who voted and their selected options (with email).
- **Regular Users**:
  - Can vote only once per poll.
  - Cannot vote before or after poll duration.
  - See results dynamically after voting.

### 🔐 Authentication
- Email-based OTP verification during registration.
- Secure login with password encryption.
- Role-based homepage redirection.

### 📊 Real-Time Results
- Results shown as list + pie chart (Chart.js).
- Auto-refresh enabled with live updates via AJAX.

---

## 🖼️ UI Snapshots

![img.png](img.png)  
![img_1.png](img_1.png)  
![img_2.png](img_2.png)  
![img_3.png](img_3.png)  
![img_4.png](img_4.png)  
![img_5.png](img_5.png)

---

## 📥 Project Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/vinayhp22/python-projects.git
cd python-projects/pollpulse
```

### 2️⃣ Create Virtual Environment
```bash
# For Linux/Mac
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database
In `PollPulse/settings.py`, configure:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pollpulse_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 📄 SQL Schema Setup

Run this from MySQL terminal:
```sql
SOURCE /absolute/path/to/schema.sql;
```
Make sure to replace `/absolute/path/to/schema.sql` with your full file path.

---

## 🔧 Run the App

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Visit:  
```
http://127.0.0.1:8000/
```

---

## 🔐 Test Accounts

| Role     | Username     | Password  |
|----------|--------------|-----------|
| Admin    | admin        | admin     |
| User     | testuser     | User@123  |
| User     | testuser1    | User@123  |

---

## 📧 Contact

For help or contributions:
- 📩 vinay@skyllx.com
- 📩 vinayhp.paramesh@gmail.com

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🗂️ Project Structure

```
PollPulse/
├── PollPulse/
│   ├── settings.py, urls.py, wsgi.py
├── polls/
│   ├── models.py, views.py, urls.py, admin.py, forms.py
│   ├── templates/polls/
│   └── static/polls/
├── media/
├── manage.py
└── schema.sql
```

---

## 📜 License

This project is licensed under the MIT License.

---

📝 **Last Updated:** April 17, 2025