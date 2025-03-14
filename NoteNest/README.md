# NoteNest

A simple yet powerful notes application built with Django and MySQL. NoteNest helps users organize their thoughts and ideas by creating, editing, deleting, and searching for notes. The app supports both global (admin-created) and user-specific categories and includes robust authentication and user management.

## Features

- **User Authentication:** Secure registration, login, and logout functionality.
- **Notes Management:** Create, edit, and delete personal notes.
- **Categorization:** Organize notes using global categories (admin-created) and user-specific categories.
- **Search Functionality:** Easily search through your notes.
- **Responsive Design:** Modern, professional UI with a responsive layout.
- **User-Specific Data:** Each user sees only their own notes and categories.

## Project Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd NoteNest
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate    # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
   
   Make sure you have Django and a MySQL client installed. For example:
   
   ```bash
   pip install django mysqlclient
   ```

4. **Database Setup:**

   - Create a MySQL database (e.g., `notenest_db`).
   - Update the `DATABASES` configuration in `NoteNest/settings.py` with your MySQL credentials.
   - **Run the `schema.sql` file** before running migrations to set up the necessary database schema:
   
     ```bash
     mysql -u your_mysql_user -p notenest_db < schema.sql
     ```

5. **Apply Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (Optional):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Server:**

   ```bash
   python manage.py runserver
   ```

   Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to use the app.

## Testing Credentials

Use the following credentials for testing purposes:

- **Admin:**
  - Username: `admin`
  - Password: `admin123`

- **Test User:**
  - Username: `testuser`
  - Password: `SkyllX@123`

## Contributions

For contributions, please contact us at vinay@skyllx.com || vinayhp.paramesh@gmail.com. We welcome and appreciate contributions from the community!

## License

This project is licensed under the terms of **SkyllX Technologies Pvt Ltd**.

![img.png](img.png)