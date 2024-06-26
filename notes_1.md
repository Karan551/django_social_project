# Django Project :-

## How To Create a Virtual environment in Python :-


```text

1.  Syntax :-  To create a virtual environment
    python3 venv environment Name 


2. To create a virtual environment(Example)
    python3 venv .venv

3. How To activate a virtual enviornement in Linux

Syntax:- source   environmentName/bin/activate

    source   .venv/bin/activate

```

## How to install Django :-
```bash
pip install django
```
-----
## How to check django version
- We can check django version in **shell prompt** , with the help of follwing command:-
  ```bash
    python3 -m django --version
  ```
- We can check via **python file** also with the following code:-
  ```python
    import django
    print(django.get_version())
  ```

-----
## How To create a project in django :-
- When we create a new project in django then we will have to take care of some initial setup. We will need generate some code that establishes a **Django project.**
- Create a folder where we we have to store our code then run the following command:-
- From the command line `cd` into a directory where we'd like to store our code and then run the following command:-<br>
- Syntax :- **django-admin startproject projectName**
  ```bash
        django-admin startproject social_project
  ```
-----

## How to runserver :-

```bash
python3 manage.py runserver
```
-----
## How To create an app in django :-

- Every time when we create an `app` then we will have **to register** this newly created app in our `django project`.
- We create an app in the following methods:-

**Syntax:-** 

- **python3 manage.py startapp appName**

```bash
python3 manage.py startapp tweetApp
```

## How To Register an app in django project :-

- Go to your project `settings.py` and **INSTALLED_APPS** list write your **appName**


*example:-*

#### **1st method:-**
```python
INSTALLED_APPS =[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # This is our app.
    'tweetApp',
]

```
-------
#### **2nd method:-**

- Otherwise Go to your app and find file name `apps.py`
and write className in `INSTALLED_APPS` 
```python
INSTALLED_APPS =[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # This is our app
    'tweetApp.apps.TweetappConfig'
]

```
-----

## How To add templates(html file) in our app :-

- Go to your app **directory/folder** and create a folder name `templates` and after creating this folder create **another folder** that name is which is your **app name** and after doing this create a file name `index.html`
- *Your path should be :-* <br>
  **tweetApp/templates/tweetApp/index.html**
  <br>
  where `tweeApp` name is our app name.

  - Go to your `views.py` file which is located in your app and write the following code:-<br>
   *path:* **tweetApp/views.py**
  ```python
  
    from django.shortcuts import render

    def index(request):
        return render(request, "tweetApp/index.html")
  
  ```

- Create another file in your app which name should be `urls.py` and write the following code:-
    ```python

    from django.urls import path
    from . import views

    urlpatterns = [
                    path("", views.index, name="index"),
                ]

    ```
