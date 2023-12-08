# Web Restaurant with Django

Restaurant Web app for list menu, booking, and see all bookings 

## Prerequisites

- Python (3.x recommended)
- Pipenv (package manager for Python)

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sukriyatma/restaurant-django.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd restaurant-django
   ```

3. **Install dependencies using Pipenv:**

   ```bash
   pipenv install
   ```

   This will create a virtual environment and install the project dependencies specified in the `Pipfile`.

4. **Activate the virtual environment:**

   ```bash
   pipenv shell
   ```

5. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The project should now be accessible at `http://127.0.0.1:8000/`.

## Configuration

- **Database:**
  - Edit the database configurations in the `settings.py` file.