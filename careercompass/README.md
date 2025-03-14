# CareerCompass

CareerCompass is a comprehensive job portal designed to connect job seekers with employers. The platform allows users to browse job listings, manage personal profiles, submit job applications, and review the status of their applications—all from a single, user-friendly interface.

## Project Features

- **Job Listings:**  
  Browse and search for jobs by category, location, or company.

- **User Profiles:**  
  Create and update profiles with details such as bio, current company, skills, and resume uploads.

- **Job Applications:**  
  Apply for jobs directly through the platform and view application statuses.

- **Company Profiles:**  
  Companies can showcase their profile and list available job positions.

- **My Applications:**  
  Authenticated users can view a list of all their submitted job applications.

- **User Authentication:**  
  Secure login, sign up, and logout functionalities.

- **Admin Panel:**  
  Manage job listings, users, and applications via Django’s admin interface.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Django  
- **Database:** MySQL  
- **Other Tools:** Git for version control

## Project Setup

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd careercompass
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows, use: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**

   - Ensure you have MySQL installed and running.
   - Create a database named `careercompass` (or update your settings accordingly).
   - **Before running the project, execute the `schema.sql` file** to set up the necessary database schema:

     ```bash
     mysql -u <username> -p careercompass < path/to/schema.sql
     ```

5. **Configure Django Settings**

   Update `careercompass/settings.py` with your MySQL credentials:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'careercompass',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }

   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

6. **Run Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

## Testing Credentials

For testing purposes, you can use the following credentials:

- **Admin:**  
  Username: `admin`  
  Password: `SkyllX@123`

- **User:**  
  Username: `vinayhp`  
  Password: `SkyllX@123`

## Project Structure

```
careercompass/
├── manage.py
├── careercompass/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── jobs/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── templates/
    │   └── jobs/
    │       ├── base.html
    │       ├── job_list.html
    │       ├── job_detail.html
    │       ├── company_profile.html
    │       ├── user_profile.html
    │       ├── edit_profile.html
    │       ├── my_applications.html
    │       └── signup.html
    └── static/
        └── jobs/
            ├── css/
            │   └── style.css
            └── js/
                └── script.js
```

## Notes

- **Media Files:**  
  Ensure that all uploaded files (e.g., resumes) are saved in the designated `media/` folder and are properly served during development.

- **Production Deployment:**  
  Configure your web server to serve static and media files. Set `DEBUG = False` in production and follow Django’s deployment checklist.

## Contact
- **For collaboration or contributions,** please contact:
vinay@skyllx.com || vinayhp.paramesh@gmail.com

## License

- **© 2025 SkyllX Technologies Private Limited. All rights reserved.**