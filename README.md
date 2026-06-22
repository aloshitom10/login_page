# Login Page

A simple Django authentication project with user registration, login, logout, and a protected dashboard page. This project demonstrates Django's built-in user model and authentication flow with clean template-based pages.

## Features

- User registration
- User login and logout
- Dashboard page after successful login
- Django authentication system
- SQLite database for local development
- Template-based HTML pages
- Static CSS support

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

```text
loginproject/
|-- loginapp/          # Main authentication app
|-- loginproject/      # Django project settings
|-- static/            # Static files
|-- db.sqlite3         # SQLite database
`-- manage.py          # Django management script
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/aloshitom10/login_page.git
cd login_page
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install Django:

```bash
pip install django
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open the app in your browser:

```text
http://127.0.0.1:8000/
```

## Usage

Register a new account, log in with your credentials, and access the dashboard. Use the logout option to end the session and return to the login page.

## Repository Topics

```text
django login auth python sqlite
```
