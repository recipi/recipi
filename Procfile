web: env PYTHONUNBUFFERED=true python manage.py runserver
worker: env PYTHONUNBUFFERED=true celery worker -A recipi.tasks -l INFO -E --autoreload -B
grunt: grunt serve

