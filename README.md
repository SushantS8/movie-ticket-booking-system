# 🎬 Movie Ticket Booking System

A Django-based movie ticket booking platform where users can browse movies, view showtimes, book and cancel tickets. Admins can manage movies and showtimes.

---

## Features

### User Features
- Browse available movies
- View showtimes for each movie
- Book seats for a showtime
- Cancel bookings

### Admin Features
- Add, update, and remove movies
- Add and manage showtimes for movies

### Validations & Safety
- Phone number validation for bookings and cancelation
- Only available seats can be booked

---

## Technologies

- Python 3.x  
- Django 4.2.x  
- SQLite (default database)  
- HTML/CSS with Django templates  
- Django forms for validation  

---

## Getting Started

### Prerequisites
- Python 3.8+  
- pip (Python package manager)  
- Virtual environment recommended

---

### Installation

1. **Clone the repository**

```bash
HTTPS - git clone [https://github.com/yourusername/movie-ticket-booking-system.git](https://github.com/SushantS8/movie-ticket-booking-system.git)
SSH - git clone git@github.com:SushantS8/movie-ticket-booking-system.git
cd movie-ticket-booking-system
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (for admin access)**

```bash
python manage.py createsuperuser
```

### Running the server

```bash
python manage.py runserver
```
- Access the application at http://localhost:8000
- Access Django admin at http://localhost:8000/admin

6. **Seed initial data (optional)**

```bash
python manage.py seed_cinema
```

### Project Structure

```bash
movie_ticket_booking_system/
├── cinema/                # Django app
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── movie_ticket_booking_system/  # Project settings
│   ├── settings.py
│   └── urls.py
├── static/                # Static assets (CSS/JS)
├── templates/             # Base templates
├── manage.py
└── requirements.txt
```


## Troubleshooting

- Ensure Python and Django versions match those in requirements.txt
- Make sure migrations are applied before running the server
- Activate virtual environment before running commands
- Check browser console if static files (CSS/JS) do not load

## Workflow

### User Workflow
1. Visit home page to browse movies
2. Click “View Showtimes” on a movie card
3. Book a seat for a showtime
4. Cancel a booking using the registered phone number

### Admin Workflow
1. Log in to Django admin panel
2. Add or remove movies and showtimes
3. Manage bookings if necessary

## Usage Notes

- Users can browse movies and showtimes without logging in.
- Booking and cancellation forms require a valid phone number.
- Admins can manage movies and showtimes via Django admin panel.

## License

This project is for educational and traineeship purposes.
