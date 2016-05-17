How to run this project?

1, Install python 2.7 
2, Install Django 1.9
3, Go into '/stock' folder, make migrations to update changes to the database.
(a) execute the command: python manage.py makemigrations
(b) then, execute: python manage.py migrate
4, Run the server, execute: python manage.py runserver
5, Open a browser and type in http://127.0.0.1:8000/

@In this project, I used SQLite3 database which is a build-in database in Django.
