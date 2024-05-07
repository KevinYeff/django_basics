<img src="https://inspector.dev/wp-content/uploads/2023/04/logo-python-django.png">

# Basics
Django is an open source framework for creating web aplicatons using Python
<img src="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/f756d96506a3f2781dd79d5f6140591a-1672321572/pfp-1/make-animated-gif-discord-logo-pfp-and-banner-gif-animation.gif" width="25" height="" alt="Perro ladrando" /> . <br>
Django allows you to create web applications quickly, simplifying a large number of repetitive tasks.
It allows you to:
- Use a database.
- Authenticate users.
- Create forms.
- Manage the security of your application.
- Have an administration panel already created.

# Installation/Requirements
This project will be done using the WSL2 Ubuntu-20.04 environment, Python 3.10.9 through a virtual environment.

```bash
nivek@YEFF:~/django_basics$ virtualenv --python=python3.10.6 venv
```
```bash
nivek@YEFF:~/django_basics$ source venv/bin/activate
(venv) nivek@YEFF:~/django_basics$ python3.10 --version
Python 3.10.9
```

## Django (Installation)
I will use Django 4.1
```bash
(venv) nivek@YEFF:~/django_basics$ pip install django==4.1
(venv) nivek@YEFF:~/django_basics$ django-admin --version
4.1
```
# Create your first project with Django!
In order to start your project you should use the following command:
```bash 
(venv) nivek@YEFF:~/django_basics$ django-admin startproject my_project
```
Or u can use the dot symbol to avoid the creation of a second folder with the same name of your project.
```bash
(venv) nivek@YEFF:~/django_basics$ django-admin startproject my_project .
```
Now in the root of your project you will have the following files:
<p align="center">

|<img src="./utils/readmeImages/explorer_1st_project.webp" width=450>|
| :---: |
|_The files shown in the image are the basic files that are created when a new Django project is created._|

</p>

> **_NOTE:** Remember that a project in Django is a high-level container, which hosts one or more applications, it also contains all the directories and files necessary for the application(s) to function properly

## Launch your project

To start your project we must take into account the file <span style="color:red;">`manage.py`</span>, this file is a script that is used to manage your Django project, this script can be used to create applications, create databases, run tests and much more.<br>
<br>So let's run the following command:

```bash
(venv) nivek@YEFF:~/django_basics$ python3 manage.py runserver
```

<p align="center">

  |<img src="./utils/readmeImages/python_manage_cmd.webp" width=850>|
  | :---: |
  |_Let's take a look at the server on which our project is running._|
  |<img src="./utils/readmeImages/python_manage_cmd_arrow.webp" width=850>|
  |_Click the link._|
  |<img src="./utils/readmeImages/first_look_project.webp" width=850>|
  |_Let's take a look at our first project!_|

</p>

As you can see our project is running at `http://127.0.0.1:8000/` <br>
Now the installation has now been successfully completed!

> Note: Remember that when executing the command you can change the port on which our project will be executed.

# Project structure

After executing the command to start a project with Django you will see a series of new files have appeared these (already seen previously), let's make a brief tour of these initial files.

- <span style="color:red;">`manage.py`</span>: This file is a script used to manage your Django project. This script can be used to build applications, create databases, run tests and much more.<br>
  For example the command we use to run our application or create the development environment: 
  ```bash
  (venv) nivek@YEFF:~/django_basics$ python3 manage.py runserver
  ```
  You can see this and other commands by executing the following command:
  ```bash
  (venv) nivek@YEFF:~/django_basics$ python3 manage.py --help
  ```
  <p align="center">

  |<img src="./utils/readmeImages/manage_help_cmd.webp" width=400>|
  |:---:|
  </p>
  Great, isn't it?

- <span style="color:red;">`db.sqlite3`</span>: It is a SQLite database that is created by default when executing the `django-admin startproject` command,
  it is used to store the data of your Django project and if necessary it can be changed to another database.

### Inside /my_project

- <span style="color:red;">`__init__.py`</span>: This is a special file that tells Python that this folder is a Python package. 
  A Python package is a collection of Python files that can be imported as a whole.

- <span style="color:red;">`asgi.py, wsgi.py`</span>: Both ASGI and WSGI are server interfaces that allow serving and running web 
  applications created with Django since these modules are better at performing this task while Django takes care of the application logic.

- <span style="color:red;">`settings.py`</span>: Roughly speaking, this file will contain the information and global configuration of the project, 
  this configuration includes things like database, secret keys, templates, password validation, the path to the folder where our static files 
  will be located, etc.

- <span style="color:red;">`urls.py`</span>: The urls.py file is one of the most important configuration files in a Django project. 
  It is responsible for mapping the application's URLs or paths to the views that handle incoming requests, it also allows the separation 
  between routing logic and views, keeping all URL routing centralized in one place.

### Flowchart

<p align="center">

|<img src="./utils/readmeImages/flowcharts/django_start_project_flowchart.png" width=750>|
|:---:|
</p>

# How to create an App with Django

In order to create an app we need to execute the following command:

```bash
venvnivek@YEFF:~/django_basics$ python3 manage.py startapp my_app
```

### Inside /my_app
- `_init_.py`: As the previous explanation it is a especial file that tells to Python that this folder is a Python package.
- `my_app/migrations`: It plays a fundamental role in Django's migration system, facilitating secure and controlled changes to the database, These changes are made automatically when we apply changes to the models of our application, thus allowing them to be synchronized.
- `admin.py`: Ths file allows us to register models in to the damin panel, giving you a graphical interface to manage app's data efficiently, the admin panel offers basic CRUD functionality as well as costomization options to tailor the admin experience to our specific needs.
- `apps.py`: A configuration file equivalent to `settings.py` from the project.
- `models.py`: This file is used to create classes that will later be converted into SQL tables, te important thing here is that Django will take care of that transition and will also do it when changes are made into the models, to achieve this Django will create migration files these will be reflected in the `my_app/migrations` folder.
- `views.py`: This file contains python functions that takes http requests and returns http response, like HTML documents.

## Your first Hello World! with Django

In order to perform this famous function but using Django, we must ake into
account the following fies from both the application and the project,
`views.py` y `urls.py` respectively.

<p align="center">

  |<img src="./utils/readmeImages/views_and_urls.png" width=200>|
  |:-:|

</p>

Now in the `views.py` file we can add methods using the request object, this
object is an indispensable tool for creating dynamic and functional views in
Django, it allow us to access to the information about the request, customize
our response, and make decisions about he view logic.
Don't forget to import and use the HttpResponse object since this will be
responsible for loading the appropiate view for the request.

```py
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello World!</h1>")
```
Wwll now that we have created the method and so that it can be sent as a
response to a client request we must, import the method and assing it to a
route in the file `urls.py`, for this example it will be the default or main
route "".

```py
from my_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('about/', views.about)
]
```
### Hello World flowchart

```mermaid
graph TD
A[Client requests primary route] --> B{Server receives request}
B --> C{Server identifies the route}
C --> D[Matches '/']
D --> E{Invokes view 'hello'}
E --> F{Receive 'request' object}
F --> G{Process the request}
G --> H{Generate HTTP response}
H --> I{Send response to client}
I --> J[Client receives response]
J --> K{Browser shows response}
```

### Reorganizing

Well, we have already learned o create our responses, at least in a basic way,
now we have to think about possibly having more applications within the 
project, which would make the list of routes very extensive, to avoid that,
we have to reorganize the views and we can do this within our app's own folder,
in fact this is what Django suggests, make the applications contain their own 
urls to simply import them and bring all the views.

In order to do this we need to also import the `include` method, this method
allows us to include routes from another url module, maing reorganization
possible and easy.


`my_project/urls.py`
```py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls'))
]
```
`my_app/urls.py`
```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
]
```


# Django - SQLite

In this section we will learn how to interact with the SQLiite database, as
well as the creation of tables from the models and their defalt tables.

In order to have access to the tables that come by default in Django we have
to execute the following commands:

```bash
venvnivek@YEFF:~/django_basics$ python3 manage.py makemigrations
```
```bash
venvnivek@YEFF:~/django_basics$ python3 manage.py migrate
```

Once these commands have been executed, we can see that our SQLite database
file now conains tables with differently composed structures.

certainly, we can't observe the content of the database file, so I recommend
to use a vscode extension called SQLite by alexcvzz.

Now from the vscode command palette or by pressing F1, we can access the SQLite
explorer, allowing us to have a view of its content.

<p>

  | <img src="./utils/readmeImages/SQLite_command_palette.png" width=382> | <img src="./utils/readmeImages/SQLite_explorer.png"> |
  |:---:|:---:|

</p>

Go ahead and take a look at your database file with the explorer.

<p align="center">
  <img src="./utils/readmeImages/SQLite_explorer_database.png" width=450>
</p>

## How to create our own tables?

Well we have already learned to use or interact with the tables that come with
Django by default, it is true that these tables are a nice help.
Naturally the project will advance and the possibility of generatig more tables
for different types of categories will become a reality, so in order to create 
our own tables, what we must take into account are the `models.py` of our app
and the `settings.py` of our project.

The first of these files will be used to create models, these will be the 
representation of the tables for the database and the second file will be used
to connect the application models with the project and thus be able to carry
out the migrations satisfactorily

Create the model in `my_app/models.py`
```py
from django.db import models

# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=200)
```

Connect the model in `my_project/settings.py`
```py
# Application definition
venvnivekyeff@nivekyeff-ThinkPad-T480:~/proyectos/django_basicspython3 manage.py migrate
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app'
]
```
Once we have created and configured the model to represent tables in the
database, we have to run the migrations, this procedure will allow us to
see the able created within the database.

We can also specify the migrations we want to do, that is, which application
we want to do the migrations for.

```bash
venvnivek@YEFF:~/django_basics$ python3 manage.py makemigrations my_app
Migrations for 'my_app':
  my_app/migrations/0001_initial.py
    - Create model Project
venvnivek@YEFF:~/django_basics$ python3 manage.py migrate my_app
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, my_app, sessions
Running migrations:
  Applying my_app.0001_initial... OK
```

<p align="center">

  <img src="./utils/readmeImages/First_model_to_SQLite_table.png" width=350>

</p>


## How to add more models/tables to the database?

To do this, we can use the same `models.py` file, if what we want is to create
more rows we have to locate the model and add more attributes that correspond
to data and if what we want is to create more tables, we need to create a new
model i.e. another class in th same file, let's create another model:

In `my_app/models.py`:
```py
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # defines relationship, deletes related data
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
```
Here, we have just defined a new model that is also related to the previous
table, now it is time to apply the migrations.

<p align="center">

  <img src="./utils/readmeImages/New_model_to_SQLite_table.png" width=350>
  <br>
  This is the resulting database after migrations.
</p>


## Interacting through the Django shell
In order to be able to interact with the tables, we can use the Django Shell,
just execute the following commnad:

```bash
venvnivek@YEFF:~/django_basics$ python3 manage.py shell
Python 3.10.9 (main, Jan 25 2024, 13:10:49) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> # import the model
>>> from my_app.models import Project, Task
>>> p1 = Project(name="movil app")
>>> p2 = Project(name="web app")
>>> # Save the project instance to the database
>>> p1.save()
>>> p2.save()
>>> # Get the projects
>>> project1 = Project.objects.get(id=1)
>>> project2 = Project.objects.get(id=2)
>>> # verify if the table exists
>>> project1
<Project: Project object (1)>
>>> # assign tasks to projects
>>> project1.task_set.create(title="Download android IDE" # description can be assigned here)
<Task: Task object (1)>
>>> project2.task_set.create(title="Download vscode")
<Task: Task object (2)>
>>> # lists tasks
>>> project1.task_set.all()
<QuerySet [<Task: Task object (1)>]>
>>> # get task by id for project1
>>> project1.task_set.get(id=1)
<Task: Task object (1)>
```

But this is somewhat tedious since every time we enter the shell, we are going
to have to import the models, assign variables over and over again, that's why
I recommend creating a script and running it from the terminal or using it as
input for the Django shell, the script will also be convenient since we can
have it as a kind of registry.

First form, running the script inside Django's shell:
```bash
venvnivek@YEFF:~/django_basics$ python3 manage.py shell
Python 3.10.9 (main, Jan 25 2024, 13:10:49) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> exec(open('<script>').read())

```
Second form, script as input:
```bash
venvnivek@YEFF:~/django_basics$ python3 manage.py shell < <script>
```
Third form, directly from terminal:
```bash
venvnivek@YEFF:~/django_basics$ cat <script> | python3 manage.py shell
```

<p align="center">

  |<img src="./utils/readmeImages/Projects_tables.png">|<img src="./utils/readmeImages/Tasks_for_projects.png" width=700>|
  |:---:|:---:|

</p>

# Consuming API for CRUD Operations on Database (Client's side (kinda :p))
Before continuing this section I want to remind you of the relationship between
the files models.py, views.py, urls.py and settings.py, we must, these files
are important for the correct development of our database, in them we can
define routes , views, models and their corresponding assignment to the main
project through configuration.

Now we have to implement an API to perform CRUD (Create, Read, Update, Delete)
operations on a database. The main view of this API is the projects function,
which is responsible for handling requests related to projects stored in the
database.

This first approach to the development of the API will be based on the
assignment of tasks for projects, that is, we will store data about projects
and assignment of tasks to carry out the project. This approach will be the
base structure of our API.

Let's get started!

The first thing we will do is, to return a good message through a request to
the database.

To do this, we will start with a fresh database, you can eliminate the database
that has surely been filled by the steps previous to this section, taking this
into account we will know that our database will be empty, in fact it does not
exist, to bring it back Back we must execute the migration commands to be able
to have the models that come by default with Django.

So, let's run them!
```bash
venvnivekyeff@nivekyeff-ThinkPad-T480:~/proyectos/django_basicspython3 manage.py makemigrations
...
venvnivekyeff@nivekyeff-ThinkPad-T480:~/proyectos/django_basicspython3 manage.py migrate
....
```
See? our database file is back, now the previous recomendation comes in handy
we are going to use the SQLite extension again to get a nice preview.

Well let's start by creating a new view, we must take into account the base of
our project, the view will serve to define a method which will send a response
back to the client, to achieve this the client will send a request to obtain
the existing projects in the database.

In the first instance, the projects table does not exist, so let's handle that so that we can send a message in response to the client request

Our app's `views.py`:

```py
from django.http import HttpResponse, JsonResponse
from .models import Project
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist

def projects(request):
  # identify the request
  if request.method == 'GET':
    try:
      # convert the objects to dict and then make a list of dictionaries
      p = list(Project.objects.values())
      # if there is no projects return a message
      if not p:
        return HttpResponse("First look, Project's table doesn't exists", status=204)
      # if project's table exists return a json representation
      return JsonResponse(p, safe=False)
    # manage the exceptions
    except DatabaseError as e:
      return JsonResponse({'error': 'Database error: ' + str(e)}, status=500)
    except ObjectDoesNotExist:
      return JsonResponse({'error': 'No projects found'}, status=404)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=500)
  # request is not GET
  else:
    return JsonResponse({'error': 'Method not allowed, GET request only'},
                        status=405)
```
Let's add an endpoint for this method in the `urls.py`:

```py
urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('projects/', views.projects) # here it is
]
```
go ahead and try to send a request you can use either postman or REST Client
extensions.

```json
HTTP/1.1 204 No Content
Date: Tue, 07 May 2024 19:23:37 GMT
Server: WSGIServer/0.2 CPython/3.10.9
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 44
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{
  "message": "First look, DataBase is empty"
}
```

# Contact

<p align="center">
  <img src="https://avatars.githubusercontent.com/u/105649198?v=4" width=135>
  <br>
  <a href="https://github.com/KevinYeff"><h>Kevin Espinoza</h></a>
</p>

<p align="center">
<a href="https://twitter.com/missingyeff" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="missingyeff" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/kevin-espinoza-salguedo-81a0a223b/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/kevin-espinoza-salguedo-81a0a223b" height="30" width="40" /></a>
<a href="https://github.com/KevinYeff" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="https://www.github.com/KevinYeff" height="30" width="40" /></a>

</p>

