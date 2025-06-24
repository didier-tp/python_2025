pip install Django 
----------------

django-admin startproject my_django_project
---> gerenate --->
my_django_project/
   manage.py
   my_django_project/
      __init__.py
      asgi.py
      settings.py
      urls.py
      wsgi.py

-------------
cd my_django_project
py manage.py migrate
py manage.py runserver
-------------
http://127.0.0.1:8000/

---------------------
python manage.py startapp my_app
--->generate my-app part :-->
├── db.sqlite3
├── my_django_project
├── manage.py
└── my_app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

---------