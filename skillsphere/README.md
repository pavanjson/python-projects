# 🎓 SkillSphere LMS

SkillSphere is a mini Learning Management System (LMS) built with Django that allows instructors to create courses and lessons, and enables students to enroll, track progress, and complete learning modules at their own pace.

---

## 🌟 Project Highlights

- 👨‍🏫 **Instructor Dashboard** to create, edit, and manage courses and lessons
- 🎓 **Student Dashboard** to enroll in courses and track lesson completion
- 📹 **Embedded Video Support** (YouTube or self-hosted)
- ✅ **Mark Lessons as Completed** with progress tracking
- 📈 **Progress Bar** on dashboard (optional future scope)
- 🎖️ **Certificate generation** on course completion (coming soon)

---

## 🧩 Technologies Used

| Layer         | Stack                                |
|---------------|---------------------------------------|
| Frontend      | HTML, CSS, Bootstrap 5                |
| Backend       | Python, Django 5.1.7                  |
| Database      | MySQL                                 |
| PDF/Cert Tool | `xhtml2pdf` or `WeasyPrint` (planned) |

---

## ⚙️ Project Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/skillsphere-lms.git
cd skillsphere-lms
```

2. **Create and activate virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # on Linux/Mac
venv\Scripts\activate           # on Windows
```

3. **Install required packages**

```bash
pip install -r requirements.txt
```

4. **Set up the database**

- Configure your MySQL database settings in `settings.py`
- Run the schema:

```bash
mysql -u root -p skillsphere_db < schema.sql
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Run the server**

```bash
python manage.py runserver
```

---

## 🧪 Testing Credentials

| Role     | Username | Password    |
|----------|----------|-------------|
| Admin    | `admin`  | `admin`     |
| Student  | `testuser` | `User@123` |
| Student  | `akshay` | `SVM@2025`  |

> You can log in and test role-based access from `/users/login/`.

---

## 🧠 App Structure

```
skillsphere/
├── courses/               # Course & lesson models, views, templates
├── users/                 # Authentication, custom user model
├── templates/             # All HTML templates
├── static/                # CSS, JS, Images
├── media/                 # Uploaded course images
├── schema.sql             # SQL script to create required tables
├── requirements.txt       # All Python dependencies
└── manage.py
```

---

## 📌 Key Features (Detailed)

- 🔒 Role-based access (Admin / Instructor / Student)
- 📚 Course creation with image/logo upload
- 🧠 Lesson content + optional video link
- 📝 Enrollments auto-created on first view
- 🚦 Student progress tracked per lesson
- ✅ Mark lessons as completed manually
- 📋 Beautiful dashboards for each user type
- 📄 Admin panel at `/admin/`

---

## 🚀 Upcoming Features

- 🎖️ Certificate generation with name/date
- 📊 Dashboard progress analytics
- 📥 Course downloads
- 🔁 Reordering lessons
- 📨 Notifications and reminders

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to contribute:

1. Fork the repo
2. Create a branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Added feature"`
4. Push and create a PR 🚀

---

## 📬 Contact

Made with ❤️ by SkyllX Technologies.  
Drop your suggestions or questions at: `vinay@skyllx.com`

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` file for details.
