# Development/Testing

## Django development server
The simples option for trying the niptviewer is to spin up a [django development server](https://docs.djangoproject.com/en/4.1/intro/tutorial01/#the-development-server),

```bash
# Fetch js and css files
bash fetch_assets.sh

# Create a virtual environment and activate it
virtualenv venv -p python3 && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup secret key
export SECRET_KEY=aJhoK81Osgg7M1M3LeNy # Set your own random string

# Setup database and admin
cd niptviewer
python3 manage.py migrate
python3 manage.py createsuperuser

# Load fixtures
python3 manage.py loaddata index
python3 manage.py loaddata sample_types

# Start development server
DJANGO_SETTINGS_MODULE=niptviewer.settingsdev python3 manage.py runserver

```

The service should now be avaible at http://127.0.0.1:8000

## Docker container

The docker development setup will create a 3 container system with the following containers:

 - [nginx](https://www.nginx.com/) service
 - web service, with niptsource code, served by [gunicorn](https://gunicorn.org/)
 - postgres database service


```bash
# Fetch js and css files
bash fetch_assets.sh

# Build image and start container
docker-compose -f docker-compose-development.yaml up --build

# Create admin user
docker exec -it {NIPT_WEB_CONTAINER_NAME_OR_ID} python manage.py createsuperuser

```

The service should now be avaible at http://127.0.0.1:8000