# **PortfolioPro**

## 🚀 Overview

**PortfolioPro** is a powerful, customizable portfolio website built with Django that enables professionals to showcase their **projects**, write **blogs**, manage **profiles**, and receive **contact messages** dynamically.  
It is designed with a **modern UI** using **Bootstrap 5**, **FontAwesome**, and **Poppins** font to create a clean and futuristic experience.

---

## ✨ Key Features

- **Professional Profile:**  
  - Showcase your **name**, **profile title**, **description**, **social links** (Facebook, Instagram, WhatsApp), and **profile picture**.
  - **Editable** directly from the dashboard.

- **Project Showcase:**  
  - Add, Edit, Delete, and **Publish/Unpublish** your projects with **image previews**.
  - Beautiful card layout for projects.

- **Blog System:**  
  - Write, edit, and delete blog posts with a clean editor.
  - Visitors can browse blogs sorted by date.

- **Contact Form with Email Sending:**  
  - Visitors can message you via a dynamic **contact form**.
  - Messages are sent to your **registered email** (SMTP configured).

- **Authentication System:**  
  - User **registration**, **login**, and **logout**.
  - Access controls to manage who can create/edit/delete content.

- **Responsive Design:**  
  - Fully responsive for desktop, tablet, and mobile.
  - Smooth animations, hover effects, and transitions.

- **Success Alerts and Validation:**  
  - Beautiful dynamic success/failure messages using Bootstrap Alerts.

- **MySQL Database Integration:**  
  - All data (users, projects, posts) stored securely in MySQL.

---

## 🛠 Project Setup

### Prerequisites
- Python 3.x
- MySQL Server
- Git (optional)
- Virtual Environment Tool (recommended)

---

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd PortfolioPro
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   - Create a MySQL database (example: `portfolio_db`).
   - Update **PortfolioPro/settings.py** with your MySQL configurations.
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```

5. **Create Superuser (Admin Account)**
   ```bash
   python manage.py createsuperuser
   ```

   - Suggested for testing:

     - **Username:** admin
     - **Password:** admin
     - **Username:** testuser
     - **Password:** User@123
     

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Open your browser:
   - Website: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔑 Admin Access and Testing

- **Admin URL:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Test Credentials:**
  - **Username:** admin
  - **Password:** admin

---

## 📁 Project Structure

```
PortfolioPro/
├── manage.py
├── PortfolioPro/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── core/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   │       └── core/
│   │           ├── base.html
│   │           ├── home.html
│   │           ├── user_profile.html
│   │           ├── portfolio.html
│   │           ├── edit_profile.html
│   │           ├── create_project.html
│   │           ├── edit_project.html
│   │           ├── delete_project.html
│   │           ├── contact.html
│   └── blog/
│       ├── admin.py
│       ├── models.py
│       ├── forms.py
│       ├── views.py
│       ├── urls.py
│       └── templates/
│           └── blog/
│               ├── blog_list.html
│               ├── blog_detail.html
│               ├── create_post.html
│               ├── edit_post.html
│               ├── delete_post.html
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── scripts.js
│   └── images/
│       └── default_profile.jpg
└── requirements.txt
```

---

## 📷 Media & Static Files

- **Static Files:**  
  `/static/` → for CSS, JS, and images (Bootstrap, FontAwesome, Custom Styling)
- **Media Files:**  
  `/media/` → for user-uploaded images (Profile Pictures, Project Images)

⚙️ Ensure you have in `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
```

---

## 📩 Email Sending (Contact Form)

- Emails sent to the user's registered email using Django's `send_mail()`.
- SMTP settings should be configured in **settings.py** (example for Gmail):
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

---

## 🔥 Special Highlights

- **Profile Edit:**  
  Update your name, email, title, bio, and even change your profile image.

- **Project Image Preview:**  
  Instantly preview uploaded images before saving.

- **Publish/Unpublish Projects:**  
  Toggle project visibility from your portfolio with one click.

- **Stylish Alerts:**  
  Dynamic success, warning, and error messages with closeable Bootstrap alerts.

- **Modern, Professional UI:**  
  Fully mobile responsive with beautiful color schemes.

---

## 📝 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

# 🚀 Ready to launch your professional portfolio?  
With **PortfolioPro**, you’re not just building a website, you’re building your brand.

