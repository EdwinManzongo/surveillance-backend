## Diarrhea Surveillance System

### SETUP

1. cd into the project folder eg cd surveillance-backend
2. create virtual environment - python -m venv <virtual-environment-name> eg python -m venv env
3. activate virtual environment - .\<virtual-environment-name>\Scripts\activate eg .\env\Scripts\activate
4. install requirement - pip install -r requirements.txt
5. make migrations - python manage.py makemigrations
6. migrate - python manage.py migrate
7. create super user - python manage.py createsuperuser
8. run server - python manage.py runserver
