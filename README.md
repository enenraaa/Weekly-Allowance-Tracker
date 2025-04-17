# 💰 Weekly Allowance Tracker

The **Weekly Allowance Tracker** is a simple **CRUD (Create, Read, Update, Delete) Django web app** that helps users track their weekly expenses and savings. It allows users to **log daily spending, calculate total expenses per week, and view overall financial summaries.** 🚀

---

## 📋 Features
✅ **Add, Edit, Delete Weeks** – Manage weekly tracking records.  
✅ **Track Daily Expenses** – Input spending for **Sunday to Saturday**.  
✅ **View Total Spent & Saved** – Automatic calculations per week.  
✅ **Manage Weekly Budget** – Set a budget and track savings.  
✅ **User-Friendly Interface** – Simple UI with Django & CSS.  

---

## 🛠️ Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS  
- **Database:** SQLite  
- **Version Control:** Git & GitHub  

---

## 🚀 Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/enenraaa/Weekly-Allowance-Tracker.git
cd Weekly-Allowance-Tracker
```

### Step 2: Set Up a Virtual Environment
```bash
python -m venv venv
```
**Activate the virtual environment:**
- Windows (PowerShell):  
`bash
venv\Scripts\activate
`

- Mac/Linux:  
``bash
source venv/bin/activate
``

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations
```bash
python manage.py makemigrations tracker
python manage.py migrate
```

### Step 5: Run the Development Server
```bash
python manage.py runserver
```

---

📂 Project Structure  
📂 Weekly-Allowance-Tracker/  
│── 📂 allowance_tracker/       `# Django project folder`  
│── 📂 tracker/                 `# Main app`  
│── 📂 templates/               `# HTML files`  
│── 📂 static/                  `# CSS styles`  
│── venv/                       `# Virtual environment (ignored by Git)`  
│── manage.py                   `# Django project manager`  
│── requirements.txt            `# Dependencies list`  
│── .gitignore                  `# Files to ignore in Git`    
│── README.md                   `# Project documentation (this file)`  

---

👨‍💻 Contributing  
Feel free to fork this repository and submit a pull request if you'd like to improve or add new features.

📜 License  
This project is licensed under the MIT License – free to use and modify.

📧 Contact
For any questions or feedback, reach out via GitHub Issues.  
⭐ If you found this project helpful, don't forget to star this repo!
