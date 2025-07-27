# Django Job Portal 🧑‍💼🖥️

A full-featured Django-based job portal with three apps:
- `users_auth_app`: User authentication, registration, and login system with a custom user model.
- `employer_app`: Employers can create company profiles, post jobs, and manage them.
- `candidate_app`: Candidates can apply for jobs, edit their application, and manage their profiles.

---

## 🌟 Features

### 🔐 User Authentication (`users_auth_app`)
- Custom user model (`customUserModel`)
- Registration, login, logout
- Redirection based on user role (admin, employer, candidate)

### 🏢 Employer Module (`employer_app`)
- Employer profile creation/editing
- Job posting (title, type, category, deadline, location, requirements)
- View, edit, and delete posted jobs
- View applicants for each job

### 👨‍💼 Candidate Module (`candidate_app`)
- Candidate profile (name, DOB, address)
- Apply to jobs
- View and edit applications
- Withdraw applications

---

## 🛠️ Technologies Used
- Django 5.2.4
- SQLite3 (default DB)
- Pillow (for image handling)
- HTML, CSS, Bootstrap (frontend)
- Python 3.12+

---

## 🚀 Installation

1. Clone the repository or extract the zip:

```bash
unzip Job-Portal_Django-main.zip
cd Job-Portal_Django-main
```

2. Create a virtual environment:

```bash
python -m venv env
source env/bin/activate  # For Windows: env\\Scripts\\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations and create superuser:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

---

## 📁 Project Structure

```
Job-Portal_Django-main/
├── job_portal_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── users_auth_app/
├── employer_app/
├── candidate_app/
├── static/
├── media/
├── manage.py
├── requirements.txt
└── LICENSE
```

---

## 📜 Requirements

```
asgiref==3.9.1
Django==5.2.4
pillow==11.3.0
sqlparse==0.5.3
tzdata==2025.2
```

---

## 👤 Author

Developed by [Khalid Mahmud](https://www.linkedin.com/in/skhalidmahmud)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).