# BlogBuzz

BlogBuzz is a feature-rich blog commenting system built using Django and MySQL, with a modern, responsive frontend using HTML, CSS, and JavaScript. It allows users to create posts, comment, like posts, search and filter posts, and includes comprehensive user authentication and administrative moderation.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Project Setup](#project-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
- [Testing Credentials](#testing-credentials)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **User Authentication:**  
  Secure login, registration, and admin access using Django’s built-in authentication.  
- **CRUD Operations:**  
  Create, read, update, and delete posts and comments.  
- **Comment Moderation & Spam Filtering:**  
  Automatic filtering for banned keywords and moderation options.  
- **Search & Pagination:**  
  Search posts by title or content and paginate results (3 posts per page by default).  
- **Tags & Likes:**  
  Add tags to posts via comma-separated input and let users like or unlike posts.  
- **Responsive & Modern Design:**  
  A professional UI featuring a sticky header with horizontal navigation and a footer at the bottom of every page.

## Technologies

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django (Python)
- **Database:** MySQL

## Project Setup

### Prerequisites

- Python 3.13.2 or above
- MySQL Server
- Virtualenv (recommended)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/BlogBuzz.git
   cd BlogBuzz
   ```

2. **Create a Virtual Environment and Activate It:**

   ```bash
   python -m venv env
   source env/bin/activate  # For Windows use: env\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database:**

   Update the `DATABASES` settings in `BlogBuzz/BlogBuzz/settings.py` with your MySQL credentials and database name (e.g., `blogbuzz_db`).

5. **Apply Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Database Setup

If you have a `schema.sql` file for initializing the database schema, run:

```bash
mysql -u your_mysql_user -p blogbuzz_db < schema.sql
```

Make sure the `schema.sql` file is located in the root directory or an appropriate folder.

6. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the Application:**

   Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Testing Credentials

- **Admin:**  
  Username: `admin`  
  Password: `admin`

- **Test User:**  
  Username: `testuser`  
  Password: `User@123`

## Contributing

Contributions are welcome! If you have improvements or bug fixes, please fork the repository and submit a pull request. For major changes, open an issue first to discuss your ideas.

## Contact

For questions, suggestions, or issues, please contact:

- **Email:** [vinay@skyllx.com](mailto:vinay@skyllx.com) || [vinayhp.paramesh@gmail.com](mailto:vinayhp.paramesh@gmail.com)
- **GitHub:** [vinayhp22](https://github.com/vinayhp22)
- **LinkedIn:** [vinayhp22](https://www.linkedin.com/in/vinayhp22/)

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Thanks to the Django community for its excellent documentation and support.
- Special thanks to all open-source projects and contributors who helped make BlogBuzz possible.
