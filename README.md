# Parking_Space_API
Python version: 3.9 \
Django test project for Parking Spaces creation/update/deletion from managers
and reservation from Employees.

# Configuration through pipenv
1. $ pip3 install pipenv
2. $ pipenv shell
3. $ pipenv install
4. $ python3 manage.py makemigrations
5. $ python3 manage.py migrate
6. $ python3 manage.py createsuperuser
7. $ python3 manage.py runserver

# Configuration through venv
1. $ pip3 install virtualenv
2. $ virtualenv test_project
3. For Linux/Mac: $ source test_project/bin/activate
4. For Windows: $ test_project\Scripts\activate
5. pip3 install -r requirements.txt
6. $ python3 manage.py makemigrations
7. $ python3 manage.py migrate
8. $ python3 manage.py createsuperuser
9. $ python3 manage.py runserver

# Configuration through docker/docker-compose
If you run first time:
$ docker-compose up --build
After:
$ docker-compose up

# Project Frameworks and libraries:
1. Django
2. Django REST Framework
3. drf-yasg
4. Pillow
5. Django Filter

# Project Description
**Django API Parking Space** created where user can pass registration selecting 
is he/she **Manager** or **Employee**. Program contains **API** from **Django 
REST Framework** and **Swagger** from **DRF-Yasg** to make frontend programmers work easier.
It also includes some tests in **tests.py** files to see if requests work properly.
Program also contains **Docker** and **Docker-Compose** so you can run project
through them.

1. Manager can create/update/delete Parking Space.
2. Employee can reserve parking space.

Also user has Profile section where he/she can add **first name, last name, 
profile image, birthday, gender and about**.
