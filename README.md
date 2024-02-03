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

