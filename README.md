# Welcome to Project Persephone

---

## Stack:
<ul>
    <li>Docker 20.10.2</li>
    <li>Docker Compose 1.28.5</li>
    <li>Django 3.2</li>
    <li>Django REST Framework 3.12</li>
    <li>Gunicorn 20.0.4</li>
    <li>PostgreSQL 13.2</li>
    <li>Redis 3.4.1</li>
    <li>Pandas 1.3.0</li>
    <li>Numpy 1.21.0</li>
    <li>Flask-SQLAlchemy</li>
    <li>DRF Generator 0.5.0</li>
    <li>Python 3.8.3</li>
</ul>

---

## How to build:

Download the content of this repository, then go inside <strong>project_persephone/src</strong> folder and run <pre>docker-compose up --build</pre> and after you hit Enter all should be set. Enjoy a cup of coffee while Docker does the work.

---

## Populate Database:

Go to <pre>checkapi/upload</pre> and upload your database dump in <strong>CSV</strong> format, table name and schema (default is public). Pandas will take care of the data and write into database.
If upload went well, you should jump to the next phase below.

---

## Generate Code

After everything is up and running, list your containers with <pre>docker container ls</pre> and get the ID from the container which has the <strong>web</strong> service in it. It should be called "src_web" or similar. After that, run the following comand to generate models for <pre>checkapi</pre> app.

<pre>python manage.py inspectdb > checkapi/models.py</pre>

Then will be the time to generate all API code:

<pre>python manage.py generate checkapi --force --depth=2</pre>

---

## Frontend

Frontend for this application is offered by Django REST Application.
