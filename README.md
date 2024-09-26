## Diarrhea Surveillance System

### SETUP

1. create virtual environment - python -m venv <virtual-environment-name> eg python -m venv env
2. activate virtual environment - .\<virtual-environment-name>\Scripts\activate eg .\env\Scripts\activate
3. install requirement - pip install -r requirements.txt
4. make migrations - python manage.py makemigrations
5. migrate - python manage.py migrate
6. create super user - python manage.py createsuperuser
7. run server - python manage.py runserver
