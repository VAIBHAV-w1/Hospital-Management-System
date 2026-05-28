Health Center — Enterprise Hospital Management System
=====================================================

Short Description
-----------------
A comprehensive, secure, and ultra-modern web-based Hospital Management System built with Django. This application provides a state-of-the-art platform for managing doctors, patients, and medical appointments efficiently with a 2026-level premium UI/UX design.

Features
--------
*   **Next-Generation UI/UX:** Built with Plus Jakarta Sans typography, deep diffused shadows, borderless interactive form inputs, and sleek rounded components for an ultra-premium feel.
*   **Dynamic Invoice Generation:** Automatically generates beautifully styled, printable medical invoices directly from successful appointment bookings.
*   **Smart Appointments Dashboard:** Real-time JavaScript filtering categorizes all appointments into "Upcoming" and "Completed" without requiring page reloads.
*   **Smooth Scroll Animations:** CSS keyframe animations (AOS-style) gracefully reveal elements as users scroll through the single-page layout.
*   **User Authentication:** Secure Registration, Login, and Email Change functionality with real-time feedback.
*   **Doctor Dashboard:** Dedicated dashboard for doctors to view and manage their upcoming schedules.
*   **RESTful API Endpoints:** Endpoints to retrieve appointment data dynamically (`/api/appointments/`, `/api/latest_appointment/`).
*   **Responsive Design:** Fully responsive layout perfectly adapting to mobile, tablet, and desktop environments.

Tech Stack
----------
*   **Backend:** Python, Django 5.0.3
*   **Frontend:** HTML5, CSS3 (Ultra-Premium Classy UI variables), Vanilla JavaScript
*   **Database:** SQLite (Development)
*   **Typography & Icons:** Plus Jakarta Sans (Google Fonts), SVG inline icons

Project Structure
-----------------
```
Hospital-Management-System/
├── Hospital/                   # Core Django app handling the models, views, and APIs.
│   ├── static/                 # Stylesheets (ui/style.css), JS scripts, image assets
│   ├── templates/              # HTML templates (base.html, index.html, appointments.html, etc.)
│   ├── models.py               # Database schemas (CustomUser, Doctor, Appointment)
│   ├── views.py                # Core logic and API endpoints
│   ├── urls.py                 # URL routing and endpoint definitions
├── PracticeHosp/               # Main Django project configuration settings.
├── manage.py                   # Django execution script
├── requirements.txt            # Package dependencies
```

Installation
------------
Follow these steps to get the project up and running on your local machine:

1. Clone the repository:
```bash
git clone https://github.com/VAIBHAV-w1/Hospital-Management-System.git
cd Hospital-Management-System
```

2. Create a Virtual Environment (Optional but recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. Install Requirements:
```bash
pip install django==5.0.3
```

4. Run Database Migrations (Ensure the database schema is up-to-date):
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the Development Server:
```bash
python manage.py runserver 9090
```

6. Access the Application:
Open your web browser and navigate to `http://127.0.0.1:9090/`

API Endpoints
-------------
*   `GET /api/appointments/`: Fetch all appointments.
*   `GET /api/latest_appointment/`: Fetch the most recently booked appointment.

Screenshots
-----------
*   **Home Dashboard:** Ultra-modern landing page combining Hero, About, Doctors, News, and Contact maps with smart smooth-scrolling anchors.
*   **Appointments Portal:** Split-screen booking form and a dedicated tracking dashboard with live-search filtering.
*   **Invoice Generator:** Dynamic printable HTML invoice popups directly from the success screen.

Author
------
Vaibhav S Wandkar
