#!/bin/sh

python3 manage.py migrate                  # Apply database migrations
python3 manage.py collectstatic --noinput  # Collect static files
python3 manage.py loaddata index
python3 manage.py loaddata sample_types
python3 manage.py runserver 0.0.0.0:8000   # run server
