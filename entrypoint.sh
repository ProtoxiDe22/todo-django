#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# collect static files so they are served properly by gunicorn
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start server
echo "Starting server..."
gunicorn --bind 0.0.0.0:8000 todo_project.wsgi:application