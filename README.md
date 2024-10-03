# Todo App

This is a simple Django-based Todo application with a PostgreSQL database, made as training project for chino.io

## Prerequisites

- Python 3.9
- Docker and Docker Compose (for running with Docker)

## Running Locally

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Copy `.env.dummy` file to `.env` in the project root and set the environment variables

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000`

## Running with Docker Compose

1. Make sure you have Docker and Docker Compose installed on your system.

2. Copy `.env.dummy` file to `.env` in the project root and set the environment variables
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
   DATABASE_NAME=postgres
   DATABASE_USER=postgres
   DATABASE_PASSWORD=postgres
   ```

3. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

4. The application will be available at `http://localhost:8000`

5. To create a superuser, use the following command:
   ```
   docker-compose exec web python manage.py createsuperuser
   ```

6. To stop the containers, use:
   ```
   docker-compose down
   ```

With docker, migrations are run automatically on build
## Project Structure

- `todo_project/`: Main Django project directory
- `todo/`: Todo app directory
- `static/`: Static files (CSS, JS, etc.)
- `templates/`: HTML templates
- `Dockerfile`: Instructions for building the Docker image
- `docker-compose.yml`: Docker Compose configuration
- `requirements.txt`: Python dependencies

## API Endpoints

The project includes a REST API with the following endpoints:

- `/api/tasks/`: List personal Tasks and create tasks (requires authentication)
- `/api/users/`: List users (requires authentication)

To use the API, you need to be authenticated. You can use the Django Rest Framework's built-in authentication views