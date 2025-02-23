# ExpenseEase - An Expense Tracker

- ### **Features:**
  - **User Authentication:** Secure register, login, and logout functionality.
  - **Expense Management:** Add, edit, and delete expense entries.
  - **Categorization:** Organize expenses into categories.
  - **Reporting:** Generate detailed reports and view an intuitive dashboard.
  - **Budget Planning:** Set budgets for different expense categories.
- ### **Advanced Features:**
  - **Export to PDF and Excel:** Easily export your reports for offline analysis.
- ### **Technologies:**
  - **Frontend:** HTML, CSS, JavaScript
  - **Backend:** Django (Python)
  - **Database:** MySQL
- ### **Brief:**
  **ExpenseEase** is a comprehensive expense tracker that helps users manage their finances by categorizing expenses, setting budgets, and generating detailed reports. With advanced export capabilities to PDF and Excel, ExpenseEase empowers you to keep track of your spending and make informed financial decisions.

---

## 📊 Expense Management

ExpenseEase allows users to add, edit, and delete expense entries quickly. Each expense can be categorized, which makes it easy to view your spending habits through detailed reports and an intuitive dashboard.

---

## 💰 Budget Planning

Plan and set budgets for each category to monitor your spending effectively. With ExpenseEase, you can compare your actual spending with your planned budgets and adjust your habits accordingly.

---

## 📈 Reporting and Analysis

Generate comprehensive reports that break down your expenses:
- **Overall Expenses:** See your total spending at a glance.
- **Month-wise Breakdown:** View detailed monthly reports.
- **Export Options:** Export each month’s report to PDF and Excel for further analysis or record-keeping.

---

## 🔧 Setup and Installation

### **Install Dependencies**

Open your terminal and run:

```bash
pip install django
pip install mysqlclient
pip install reportlab xlwt
```

### **Database Setup**

1. **Install MySQL** and create a new database for ExpenseEase.
2. **Update your database settings** in `ExpenseEase/settings.py` with your MySQL credentials.
3. Run the following commands to set up your database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### **Running the Application**

Start the Django development server by running:

```bash
python manage.py runserver
```

Then navigate to `http://127.0.0.1:8000/` in your browser.

---

## 🔑 Default Login Credentials

Use the following login credentials for testing:  
**Username:** `admin`  
**Password:** `SkyllX@123`  

To create an admin account, run:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

---

ExpenseEase provides a powerful and user-friendly expense tracking experience with intuitive budgeting, detailed reporting, and export functionality. Manage your finances with ease and take control of your spending today!

---
