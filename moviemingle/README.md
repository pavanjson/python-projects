# 🎬 MovieMingle

MovieMingle is a full-featured Django web application that lets users explore, rate, and review movies — while admins can manage the movie database. Built with Django, MySQL, and Bootstrap, it delivers a modern user experience with role-based access, personalized favorites, and dynamic search.

---

## 🚀 Project Features

- 🔍 **Movie Search** — Filter movies by title instantly
- 🎞️ **Add/Edit/Delete Movies** (Admin only)
- ⭐ **Rate & Review** — Users can rate a movie once and update/delete it anytime
- ❤️ **Favorites List** — Build your own movie collection
- 🧑‍💻 **Authentication** — Role-based dashboard: admin vs user
- 📄 **Pagination** — Browse cleanly through movie listings
- 📱 **Responsive UI** — Powered by Bootstrap 5

---

## 🗂️ Project Structure

```
moviemingle/
│
├── moviemingle/              # Django project
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── movies/                   # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/movies/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── movie_detail.html
│   │   ├── movie_form.html
│   │   ├── edit_review.html
│   │   └── delete_review.html
│   └── static/movies/
│       └── css/style.css
│
├── schema.sql                # SQL dump to prefill database
├── db.sqlite3 / MySQL        # Database file (depending on use)
└── manage.py
```

---

## 🛠️ Technologies Used

- **Backend**: Django 5.1.7 (Python 3.13+)
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Authentication**: Django auth with superuser/user roles

---

## 🧪 Testing Credentials

| Role   | Username   | Password      |
|--------|------------|---------------|
| Admin  | `admin`    | `admin`       |
| User   | `testuser` | `User@123`    |

> You can log in and explore the site as an admin or a test user.

---

## ⚙️ Project Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/vinayhp22/python-project.git
   cd moviemingle
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MySQL database**
   In `settings.py`, update the database settings:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'moviemingle_db',
           'USER': 'root',
           'PASSWORD': 'yourpassword',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Run SQL script to populate initial data**
   ```bash
   mysql -u root -p moviemingle_db < schema.sql
   ```

6. **Apply migrations and run server**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

---

## 📬 Feedback or Suggestions?

We welcome contributions, suggestions, and movie lovers! Open a PR or raise an issue.
Drop a mail [Vinay @ SkyllX](mailto:vinay@skyllx.com) || [Vinay H P](mailto:vinayhp.paramesh@gmail.com)

---

## 📄 License

MIT License. © 2025 [SkyllX Technologies Pvt Ltd](www.skyllx.com)
