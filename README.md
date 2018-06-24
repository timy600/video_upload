# ENVIRONMENT CONFIGURATION

- Create venv with python3
python3 -m venv ./virtual_env

- Activate the virtual env
source ./virtual_env/bin/activate

- Upgrade pip
pip install --upgrade pip

- installation pip module (ex: django)
pip install django

- pip installation from requirement.txt
pip install -r requirement.txt

- create requirement.txt including all module already installed on virtual env
pip freeze > requirement.txt


# DATABASE CONFIGURATION

The database used is SQLite3, before starting the server a first migration is required with the following commands:
python manage.py makemigrations
python manage.py makemigrations app
python manage.py migrate

# USING THE REST-API

The app is now ready to be launched:
python manage.py runserver

If no Frontend app has been designed, Postman can be used to test the routes, the main one being a post request with a name and a file (video).
