# ArtyProd - Production Artist Portfolio and Management Platform

## Description

ArtyProd is a comprehensive Django-based web application designed to showcase the work of production artists and facilitate project management. It provides a robust platform for artists to display their portfolios, for clients to browse and request services, and for administrators to manage projects, clients, and artists effectively.

## Features

*   **Artist Portfolio Management:** Artists can create and manage their profiles, upload their work, and categorize their projects.
*   **Client Management:** Clients can browse artist portfolios, submit project requests, and track the status of their projects.
*   **Project Management:** Administrators can create, assign, and track projects, manage project phases, and allocate resources.
*   **User Authentication and Authorization:** Secure user registration, login, and role-based access control for artists, clients, and administrators.
*   **RESTful API:** A well-defined API for programmatic interaction with the platform.
*   **Admin Interface:** A user-friendly administrative interface (powered by Django Jazzmin) for managing all aspects of the application.
*   **Payment Integration:** (Potentially) Integration with PayPal for handling payments.

## Technologies Used

*   **Backend:** Django, Django REST Framework
*   **Database:** SQLite (default, can be configured for PostgreSQL/MySQL)
*   **Frontend:** HTML, CSS, JavaScript (Django's templating engine)
*   **Styling & UI:** Django Jazzmin, Django Crispy Forms, Django Widget Tweaks
*   **Other Python Libraries:** arabic-reshaper, Pillow, pyhanko, qrcode, reportlab, xhtml2pdf, etc. (See `requirements.txt` for a complete list)

## Installation

To get a copy of this project up and running on your local machine for development and testing purposes, follow these steps.

### Prerequisites

*   Python 3.x
*   pipenv (recommended for dependency management)

### Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/A-Hamdi1/ArtyProd.git
    cd ArtyProd
    ```

2.  **Create a virtual environment and install dependencies:**

    ```bash
    pipenv install
    pipenv shell
    ```
    If you prefer to use `pip` directly:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Apply database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Create a superuser (for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

*   **Admin Panel:** Access the Django administration panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.
*   **Client Interface:** Clients can register, log in, browse artists, and submit project requests.
*   **Artist Interface:** Artists can manage their profiles, upload projects, and view assigned tasks.

## Project Structure

```
ArtyProd/
├── artyprod/                  # Main Django project configuration
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL routing
│   ├── wsgi.py                # WSGI configuration
│   ├── asgi.py                # ASGI configuration
│   ├── juzmin.py              # Custom Jazzmin admin configuration
│   └── templates/             # Project-level templates
├── artyweb/                   # Core Django application for portfolio and project management
│   ├── admin.py               # Admin panel customizations
│   ├── apps.py                # Application configuration
│   ├── forms.py               # Django forms
│   ├── models.py              # Database models
│   ├── serializers.py         # Django REST Framework serializers
│   ├── urls.py                # Application URL routing
│   ├── views.py               # Application views (logic)
│   ├── templatetags/          # Custom template tags
│   ├── templates/             # Application-specific templates
│   ├── static/                # Static assets (CSS, JS, images)
│   └── migrations/            # Database migration files
├── media/                     # User-uploaded media files
├── staticfiles/               # Collected static files (for deployment)
├── requirements.txt           # Python dependencies
├── manage.py                  # Django management script
├── db.sqlite3                 # Default SQLite database file
├── Procfile                   # For Heroku deployment
└── README.md                  # Project README file
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details. (Assuming MIT, you might want to create this file if it doesn't exist) 
