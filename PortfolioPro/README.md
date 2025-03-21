# PortfolioPro

## Overview

PortfolioPro is a dynamic portfolio website that enables professionals to showcase their projects, share experiences, and connect with potential clients or employers. The project is built using Django for the backend, HTML/CSS/JavaScript for the frontend, and MySQL for data storage.

**Key Features:**
- **Personal Profile & Project Showcase:** Display your projects with images, descriptions, and status (published/unpublished).
- **Blog Section:** Create, edit, and delete blog posts.
- **Contact Form:** Allow visitors to reach out with inquiries.
- **Authentication:** Secure login/logout, with admin and user access for creating/editing content.

## Project Setup

### Prerequisites
- Python 3.x installed
- MySQL server installed and running
- Git (optional, for cloning the repository)
- Virtual environment tool (recommended)

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd PortfolioPro
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup:**
   - Create a MySQL database (e.g., `portfolio_db`).
   - Update the database configuration in `PortfolioPro/settings.py` with your MySQL credentials.
   - Run Django migrations:
     ```bash
     python manage.py migrate
     ```
   - **Optional:** If provided, execute the SQL script to initialize the database schema:
     ```bash
     mysql -u your_mysql_user -p portfolio_db < schema.sql
     ```

5. **Create a Superuser for Admin Access:**
   ```bash
   python manage.py createsuperuser
   ```
   - For testing purposes, you can use:
     - **Username:** admin
     - **Password:** admin

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the main site and [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) for the admin panel.

## Admin Access & Testing Credentials

- **Admin Panel URL:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Testing Credentials:**
  - **Username:** admin
  - **Password:** admin

## Project Structure

```
PortfolioPro/
├── manage.py
├── PortfolioPro/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── templates/
│   │       └── core/
│   │           ├── base.html
│   │           ├── home.html
│   │           ├── about.html
│   │           ├── portfolio.html
│   │           └── contact.html
│   └── blog/
│       ├── __init__.py
│       ├── admin.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── templates/
│           └── blog/
│               ├── blog_list.html
│               └── blog_detail.html
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── scripts.js
│   └── images/
│       ├── about.jpg
│       ├── project1.jpg
│       └── project2.jpg
└── requirements.txt
```

## Media & Static Files

- **Static Files:** Served from the `/static/` URL.
- **Media Files:** Uploaded images are served from the `/media/` URL (ensure `MEDIA_ROOT` and `MEDIA_URL` are configured in `settings.py`).

## Additional Information

- **Schema Initialization:**  
  If you have a `schema.sql` file, run it against your MySQL database to set up the initial schema.
- **Testing:**  
  After setting up, log in with the provided admin credentials to verify functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


