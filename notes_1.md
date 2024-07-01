# Django Project :-

## How To Create a Virtual environment in Python :-


```text

1.  Syntax :-  To create a virtual environment
    python3 -m venv environment Name 


2. To create a virtual environment(Example)
    python3 -m venv .venv

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
------
## How To Add Static Files (CSS , JavaScript) in Our App :-

- This is also similar to add `templates` in our **django app**.
  
  #### To Add CSS File :-
  - Go to your app **directory/folder** and create a folder name `static` and after creating this folder create **another folder** that name is which is your **app name** and after doing this create another folder which name is `css` and inside `css` folder create a **css file** `styles.css`
  - *Your path should be :-* <br>
    **tweetApp/static/tweetApp/css/styles.css**
    <br>
    where `tweeApp` name is our app name.

  - **styles.css** file is:-👇
 
    ```css
      body{
        background-color:red;
          color:green;
      }
    ```

  #### To add JavaScript File :-
  - Go to your app **directory/folder** and create a folder name `static` and after creating this folder create **another folder** that name is which is your **app name** and after doing this create another folder which name is `js` and inside `js` folder create a **js file** `main.js`
  
  - *Your path should be :-* <br>
    **tweetApp/static/tweetApp/js/main.js**
    <br>
    where `tweeApp` name is our app name.

  - **main.js** file is:-👇
      ```javascript
          console.log("Hello Django.")
      ```

- And `index.html` file is:-👇
   ```html
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Django Project</title>
          <!-- Here we will add css file -->
          <link rel="stylesheet" href="{% static 'tweetApp/css/myStyle.css' %}">
          </head>
          <body>

          <h2>Hello Django</h2>

          <!-- Here we will add js file. -->
          <script src="{% static 'tweetApp/js/main.js' %}"></script>
  
          </body>
          </html>
    ```
------


## How To Add templates (html) files in *Project root directory* :-

- `root` directory means where `manage.py` file is located. Which is also known as **BASE_DIR (Base Directory)**. 
- We can **print** variable name **BASE_DIR** that is located our `settings.py` file.
- To **add templates** in our **Project root directory** follow these steps :-
  
    1. &nbsp; Create a folder (directory) which name is `templates` in our **BASE_DIR** or **root directory**.
    2. &nbsp; Inside `templates directory` create any file which name mostly `index.html`. In `index.html` file write your **html code.**
    3. &nbsp; After writing html code . Go To your `settings.py` file and write  `DIRS:['templates']`, **DIRS** mean Directory that value is **templates** directory.  
   
         <h3 align="center" style="text-decoration:underline">1st method:-</h3>
         
         - **path:- 👉**   ***project_directory/settings.py***
         - For Example 👉   **social_project/settings.py**
       
  
  ```python
            
  TEMPLATES = [
    {
  'BACKEND':'django.template.backends.django.DjangoTemplates',
  # Here we write 'templates'
  'DIRS': ['templates'],
  'APP_DIRS': True,
  'OPTIONS': {
            'context_processors':[
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    ]
  ```      
  <h3 align="center" style="text-decoration:underline">2nd method:-</h3>

  - First we will have to `import os` module and add <br>  `DIRS:[os.path.join(BASE_DIR,'templates')]`
  
  ```python

  import os
  
  TEMPLATES = [
    {
  'BACKEND':'django.template.backends.django.DjangoTemplates',
  # Here we write 
  'DIRS': [os.path.join(BASE_DIR,'templates')],
  'APP_DIRS': True,
  'OPTIONS': {
            'context_processors':[
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    ]

  ```

------
## How To Add Static Files (CSS , JavaScript) in Our Project Root Directory :-

- Go To our project `settings.py` file and add the following code in `settings.py` file 
<h4 align="center" style="text-decoration:underline">1st method :- </h4>

- In **settings.py** file 👇
```python

  STATIC_URL = "static/" # below this line add the following line of code
  
  STATICFILES_DIRS = [
                      BASE_DIR / "static",
                  ]
```

<h4 align="center" style="text-decoration:underline">2nd method :- </h4>

- Otherwise we have to **import os module** and write the following line of code in our `settings.py` file.
- In **settings.py** file 👇
  ```python
  import os

  STATIC_URL = "static/" # below this line add the following line of code
  
  STATICFILES_DIRS = [
                      os.path.join(BASE_DIR,"static"),
                  ]

  ```

  #### To add css file :-
  -  Create a folder in our project **root directory** which name is `static` inside `static` folder create another folder which name is `css` and inside css folder create a file which name is `style.css`
  -  *Syntax :-* 👉 &nbsp;  **project_root_directory/static/css/style.css**
  -  *path :-* 👉 &nbsp; **social_project/static/css/style.css**
  -  **style.css** &nbsp; file is :- 👇
      ```css
        body{
            background-color:red;
          }
      ```

  #### To add JavaScript file :-
  - Create a folder in our project **root directory** which name is `static` inside `static` folder create another folder which name is `js` and inside js folder/directory create a file which name is `index.js`
     - *Syntax :-* 👉 &nbsp;  **project_root_directory/static/js/index.js**
     -  *path :-* 👉 &nbsp; **social_project/static/js/index.js**
     -  **index.js** &nbsp; file is :- 👇
         ```javascript
         console.log("Hello Django.");
         ```

- And inside **templates directory** in `index.html` file at the top of the file write `{% load static %}` **to load static file** in our html file. 
  ```html
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />

      <!-- Here We link css file -->
      <link rel="stylesheet" href="{% static 'css/styels.css' %}">

      <title>
      {% block title %}Django Social App{% endblock title %}

      </title>
  
    </head>
    <body>

      {% block content %}{% endblock content %}

      <!-- Here we link javascript file -->
      <script src="{% static 'js/index.js' %}"></script>
    </body>
  </html>
  ```



  
 
------


## How To Create an admin User :-

- We will have to create a user who can login an admin site.To do this we will have to run the following command in our terminal:-
  ```bash
      python3 manage.py createsuperuser
  ```
- Enter your desire **username**, **email address** and **password** also. After enter your information press enter and You will see a message `Superuser created sucessfully.`
- After creating `superuser` start development server and open a browser and go to `/admin/` on your local domain <br>
  **example :-** **http://127.0.0.1:8000/admin** <br> Then you will show admin's login screen.