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

---

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

---

## How To freeze a pip :-

- Every time when we **install** a **new library / package or framework** then we will have to freeze our `pip` with the following command -
- Syntax :- 👉 &nbsp; **pip freeze > path**
  ```bash
  pip freeze > ../requirements.txt
  ```
- It's recommended to create a **requirements.txt** file in your directory where your project are located **requirements.txt** file tells us what dependicies are required to our project.
- It's optional but recommended to production grade applications.

---

## How To create a project in django :-

- When we create a new project in django then we will have to take care of some initial setup. We will need generate some code that establishes a **Django project.**
- Create a folder where we we have to store our code then run the following command:-
- From the command line `cd` into a directory where we'd like to store our code and then run the following command:-<br>
- Syntax :- **django-admin startproject projectName**
  ```bash
        django-admin startproject social_project
  ```

---

## How to runserver :-

```bash
python3 manage.py runserver
```

---

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

_example:-_

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

---

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

---

## How To add templates(html file) in our app :-

- Go to your app **directory/folder** and create a folder name `templates` and after creating this folder create **another folder** that name is which is your **app name** and after doing this create a file name `index.html`
- _Your path should be :-_ <br>
  **tweetApp/templates/tweetApp/index.html**
  <br>
  where `tweetApp` name is our app name.

  - Go to your `views.py` file which is located in your app and write the following code:-<br>
    _path:_ **tweetApp/views.py**

  ```python

    from django.shortcuts import render

    def index(request):
        return render(request, "tweetApp/index.html")

  ```

  - `render()`:- **render()** function **takes the request object as its first argument**, **a template name as its second argument** and **a dictionary as its optional third argument.** It returns an `HttpResponse` object of the given template rendered with the given context.
  - Syntax:-👉 &nbsp;`render(request,template_name,{})`
  - **Example :-** 👉 &nbsp;**render(request,"index.html", { "name" : "Master" } )**

- Create another file in your app which name should be `urls.py` and write the following code:-

  ```python

  from django.urls import path
  from . import views

  urlpatterns = [
                  path("", views.index, name="index"),
              ]

  ```

---

## How To Add Static Files (CSS , JavaScript) in Our App :-

- This is also similar to add `templates` in our **django app**.

  #### To Add CSS File :-

  - Go to your app **directory/folder** and create a folder name `static` and after creating this folder create **another folder** that name is which is your **app name** and after doing this create another folder which name is `css` and inside `css` folder create a **css file** `styles.css`
  - _Your path should be :-_ <br>
    **tweetApp/static/tweetApp/css/styles.css**
    <br>
    where `tweetApp` name is our app name.

  - **styles.css** file is:-👇

    ```css
    body {
      background-color: red;
      color: green;
    }
    ```

  #### To add JavaScript File :-

  - Go to your app **directory/folder** and create a folder name `static` and after creating this folder create **another folder** that name is which is your **app name** and after doing this create another folder which name is `js` and inside `js` folder create a **js file** `main.js`

  - _Your path should be :-_ <br>
    **tweetApp/static/tweetApp/js/main.js**
    <br>
    where `tweetApp` name is our app name.

  - **main.js** file is:-👇
    ```javascript
    console.log("Hello Django.");
    ```

- And `index.html` file is:-👇

  ```html
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Django Project</title>
      <!-- Here we will add css file -->
      <link rel="stylesheet" href="{% static 'tweetApp/css/myStyle.css' %}" />
    </head>
    <body>
      <h2>Hello Django</h2>

      <!-- Here we will add js file. -->
      <script src="{% static 'tweetApp/js/main.js' %}"></script>
    </body>
  </html>
  ```

---

## How To Add templates (html) files in _Project root directory_ :-

- `root` directory means where `manage.py` file is located. Which is also known as **BASE_DIR (Base Directory)**.
- We can **print** variable name **BASE_DIR** that is located our `settings.py` file.
- To **add templates** in our **Project root directory** follow these steps :-

  1. &nbsp; Create a folder (directory) which name is `templates` in our **BASE_DIR** or **root directory**.
  2. &nbsp; Inside `templates directory` create any file which name mostly `index.html`. In `index.html` file write your **html code.**
  3. &nbsp; After writing html code . Go To your `settings.py` file and write `DIRS:['templates']`, **DIRS** mean Directory that value is **templates** directory.

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

  - First we will have to `import os` module and add <br> `DIRS:[os.path.join(BASE_DIR,'templates')]`

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

---

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

  - Create a folder in our project **root directory** which name is `static` inside `static` folder create another folder which name is `css` and inside css folder create a file which name is `style.css`
  - _Syntax :-_ 👉 &nbsp; **project_root_directory/static/css/style.css**
  - _path :-_ 👉 &nbsp; **social_project/static/css/style.css**
  - **style.css** &nbsp; file is :- 👇
    ```css
    body {
      background-color: red;
    }
    ```

  #### To add JavaScript file :-

  - Create a folder in our project **root directory** which name is `static` inside `static` folder create another folder which name is `js` and inside js folder/directory create a file which name is `index.js`
    - _Syntax :-_ 👉 &nbsp; **project_root_directory/static/js/index.js**
    - _path :-_ 👉 &nbsp; **social_project/static/js/index.js**
    - **index.js** &nbsp; file is :- 👇
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
      <link rel="stylesheet" href="{% static 'css/styels.css' %}" />

      <title>{% block title %}Django Social App{% endblock title %}</title>
    </head>
    <body>
      {% block content %}{% endblock content %}

      <!-- Here we link javascript file -->
      <script src="{% static 'js/index.js' %}"></script>
    </body>
  </html>
  ```

---

## How To Create an admin User :-

- We will have to create a user who can login an admin site.To do this we will have to run the following command in our terminal:-
  ```bash
      python3 manage.py createsuperuser
  ```
- Enter your desire **username**, **email address** and **password** also. After enter your information press enter and You will see a message `Superuser created sucessfully.`
- After creating `superuser` start development server and open a browser and go to `/admin/` on your local domain <br>
  **example :-** **http://127.0.0.1:8000/admin** <br> Then you will show admin's login screen.

---

## What is view in Django :-

- A **view** is a "type" of webpage in our Django web application that **generally serves a specific function** and has a specific **template**.
- In Django, **web pages and other content** are **delivered by views**. **Each view** is represented by a **python function** (or method in the case of class based views). Django will choose a view by examine a URL that's requested.
- To get from a URL to a view, Django uses what are known as **URLconfs**. A URL confs maps URL pattern to views.
- _For example_ 👇:- &nbsp; In a **blog application** you might have the following views:
  - **Blog homepage** - _displays latest few entries._
  - **Entry "detail" page** - _permalink page for a single entry._
  - **Comment Action** - _handling post comments to a given entry._ <br> and so on.

---

## How To capture a value that comes via url (url bar) :-

- **To get a value from a url bar** which is known as **permalink or slug**.
- open a file which name is `urls.py`

  ```python
  from django.url import path

  urlpatterns = [
    # home page.
    path("", views.index, name="index"),
    # example : /5
    path("<int:question_id>/", views.detail, name="detail"),

    # example: /5/results/
    path("<int:question_id>/results/", views.results, name="results"),

    # example: /5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

  ]
  ```

- **Using angle brackets** "captures" part of the **URL** and send it as a keyword argument to the view function. The question_id **part of the string** **defines the name that will be used to identify the matched pattern**, and the **int** part **is a converter** that determines what patterns should match this part of the **URL path**.
- The **colon(:)** **seprates** the **converter** and **pattern name (variable name)**.
- **Syntax :-** 👉&nbsp;`<converter:variableName>`
- example :- `<int:id>`

  #### Note :-

  - **To capture a value from a URL use angle brackets**.
  - **Captured value can be optionally include a converter type**.
  - **For example**, use `<int:name>` to **capture an integer parameter**. If **a converter** **isn’t included, any string, excluding a / character, is matched**.
  - **There’s no need to add a leading slash, because every URL has that**.

  ### Path Converters :-

  - The follwing path converteres are available by default :-

    1. &nbsp;**str :-** _Matches any non-empty string, excluding the path separator, '/'. This is the default if a converter isn’t included in the expression._
    2. &nbsp;**int :-** _Matches zero or any positive integer. Returns an int._
    3. &nbsp;**slug :-** Matches any **slug string consisting** of **ASCII letters** or **numbers, plus the hyphen and underscore characters**. ,<br> For example :- _building-your-1st-django-site_.
    4. &nbsp;**path :-** **Matches any non-empty string, including the path separator, '/'.** This allows you to match against a complete URL path rather than a segment of a URL path as with str.
    5. &nbsp;For more information [click here.](https://docs.djangoproject.com/en/5.0/topics/http/urls/)

- Wire these `urls.py` file with `views.py` file .

  ```python
  def detail(request,question_id):
    return HttpResponse("You're looking at question",question_id)

  def results(request,question_id):
    return HttpResponse("You're looking at the result of question",question_id)

  def vote(request,question_id):
    return HttpResponse("You're voting on question",question_id)
  ```

---

## Django Shortcut Functions :-

1.  &nbsp;**render():-** This function is used to render a html file in a browser.<br/>
    &nbsp;**Syntax :-** **render(request,template_name,context)** <br/>
    **required arguments:-**

    - **request :-** The request object used to generate this response.
    - **template_name :-** The full name of a template to use or sequence of template names(html file).

    **optional arguments :-**

    - **context :-** **A dictionary of values** to add to the **template context.** **By default, this is an empty dictionary.** If a value in the dictionary is callable, the view will call it just before rendering the template.

2.  &nbsp;**redirect() :-** Returns an `HttpResponseRedirect` to the **appropriate URL for the arguments passed.**
3.  &nbsp;**get_object_or_404() :-** This function calls `get()` on a `given model manager`, **but it raises Http404 instead of the model’s DoesNotExist exception.** <br/>

    - This function takes a **Django Model as a first argument** and **an arbitary number** of **keyword number of arguments** which it passes to the **get() function** of the **model's manager.** It **raises** `Http404` if the object doesn't exist.
    - **Syntax :-** 👉 `get_object_or_404(Model_name,Lookup_parameter)`
    - **Example :-** 👉 &nbsp;**get_object_or_404(Question, pk=question_id)**

4.  &nbsp;**get_list_or_404() :-** This function returns the result of `filter()` on a **given model manager cast to a list,** **raising Http404** if the result **list is empty.**
    - **Syntax :-** 👉 `get_list_or_404(Model_name,Lookup_parameter)`
    - **Example :-** 👉 &nbsp;**get_list_or_404(Question, pk=question_id)**
5.  &nbsp;For more information [click here](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/)

---

## Namespacing URL names :-

- If your project just has **one app** then no need **Namespacing URL names.**
- In real Django projects there might be five, ten or twenty apps or more. How does Django differentiate the URL names between them ?
- To get rid of this problem **Django use namespacing URL.**
- **Syntax :-** 👉 &nbsp;**app_name = "application_name"**
- In our application `urls.py` file we add **namespacing URL.**
- file 👇 **urls.py** add the following code :-

  ```python
  from django.urls import path

  # this will add
  app_name = "tweetApp"

  urlpatterns = [
    path("", views.index, name="index"),

    ]
  ```

- After doing this we have to change **link or path** in HTML file.
- **Syntax:-** 👉 &nbsp;**{% url 'appName:view_function'  URLconf (optional)  %}**
- _file_ 👇&nbsp;**tweetApp/templates/tweetApp/index.html**

  ```html
  <a href="{% url 'tweetApp:index' %}">Click Here</a>
  ```

---

## How To check that which route is active and change CSS in nav bar :-

- `request.resolver_match.url_name` gives us **current route.**

```python
<a class="nav-link {% if request.resolver_match.url_name == 'about' %}active{% endif %}" aria-current="page" href="{% url 'polls:about' %}">About Us</a>
```

---

### Some Important Notes :-

- `reqest.method == "POST"` 👉 It is used **to check** that `request` is **POST or not.**
- `reques.method == "GET"` 👉 It is used **to check** that request is **GET or not.**
- `request.user` 👉 This gives us **registered user value.**
- `request.POST` 👉 It is a **dictionary** that is used only **POST request.**
- `request.GET` 👉 It is also a **dictionary** but it is used only **GET request**.
- `request.POST['key-name']` 👉 This gives us value that we wiil give in front-end section.
  - **[ 'key-name' ]** 👉 It is value of name attribute value in HTML page.
- `request.GET['key-name']` 👉 Similar to `request.POST['key-name']` but it is used only **get request**.
- `LOGIN_URL` **:-** 👉 **The URL or named URL pattern where requests are redirected for login** when using the `login_required()` **decorator**. <br> **Default value of this constant** is `/accounts/login/` , **This constant we write** in `settings.py` file.
  - **Syntax :-** 👉 **LOGIN_URL = url Or named_url**
  - **For example :-** 👉 `LOGIN_URL = "tweet_app:login"`
- `LOGIN_REDIRECT_URL` **:-** 👉 **The URL or named URL pattern where requests are redirected after sucessfully login when the LoginView doesn’t get a next GET parameter.** <br> **Default value of this constant** is `/accounts/profile/` , **This constant we write** in `settings.py` file.

- `LOGOUT_REDIRECT_URL` **:-** 👉 **The URL or named URL pattern where requests are redirected after logout if LogoutView doesn’t have a next_page attribute.** <br> **Default value of this constant** is `None` , **This constant we write** in `settings.py` file.

  - [Click Here](https://docs.djangoproject.com/en/5.0/ref/settings/#login-redirect-url) for more information.

---

## How To Create a Private Route/View :-

- **Syntax :-** &nbsp;
  `login_required(redirect_field_name='next', login_url=None)`

  1. `redirect_field_name` :- 👉 &nbsp; **This argument tells us what we want to do after sucessufully logged in.**

     - `redirect_field_name = 'next'` **(By default) but we can overwrite this.**

  2. `login_url` :- 👉 &nbsp; This argument tells us where we want to carry our private route. **By Default it is** `None`.
     - for example :- `tweet_create -> tweet_app:login`

  - If the **user isn’t logged** in, **redirect** to **settings.LOGIN_URL**, passing the current absolute path in the query string.

  - If the **user is logged in**, **execute the view normally**. The view code is free to assume the user is logged in.

- We can create a private route with the help of `
@login_required` **decorator**

<h2 align="center">1st method</h2>

```python

from django.contrib.auth.decorators import login_required

# the route / function that we want to make private.

@login_required
def tweet_create(request):
  form = TweetForm()
  if request.method == "POST":
      form = TweetForm(request.POST, request.FILES)
      if form.is_valid():
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect("/")

  else:
      return render(request, "tweetApp/tweet_create.html", {"form": form})

```

- After doing this we will go in `settings.py` file in our project directory.
- `settings.py` 👇 **file**

  ```python
   # This will handle private route.
  LOGIN_URL = "tweet_app:login"

  # Redirect after login to main page.
  LOGIN_REDIRECT_URL = "/"
  ```

  <h2 align="center">2nd method</h2>

  - In this method we can **directly pass an argument** in the `@login_required` **decorator**
  - In `views.py` **file** 👇

    ```python
    from django.contrib.auth.decorators import login_required

    @login_required(redirect_field_name="/", login_url="tweet_app:login")
    def tweet_create(request):
    form = TweetForm()
    if request.method == "POST":
      form = TweetForm(request.POST, request.FILES)
      if form.is_valid():
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect("/")

    else:
      return render(request, "tweetApp/tweet_create.html", {"form": form})

    ```

- [Click here](https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-login-required-decorator) for more information.

---

## How To add environment variables in Django :-

- **Step :-1** 👉 &nbsp; Create a `.env` file in **project root directory** or `BASE_DIR` , In simple terms we can say that where `manage.py `file is located.

- **Step :-2** 👉 &nbsp; And Write Your all credentials in `.env` file.

  - **For example :-** 👇

    ```text
      DATABASE_NAME = 'your_database_name'
      DATABASE_PASSWORD = 'your_database_password'

      SECRET_KEY = 'your_secret_key'
    ```

- **Step :-3**
    <h3 align="center">1st Method </h3>

  - First And Firemost We have to install this module :-

    ```bash
    pip install python-dotenv

    # or type this command
    pip3 install python-dotenv
    ```

  - Anywhere in our project where we want to use our credentials that we have written in `.env` file. We can use this in the following way :-

    ```python
    import os
    from dotenv import load_dotenv,dotenv_values

    # To load all config from .env
    load_dotenv()

    # To get credentials (Syntax) -> os.getenv('key_name')
    print(os.getenv('DATABASE_PORT'))

    # Another method

    print(os.environ.get('DATABASE_NAME'))

    # Otherwise we create dictionary and further we get values from that dictionary.
    conf = dotenv_values()

    print(conf['DATABASE_NAME'])

    ```

  - If we have not written our credentials in string format then we have to convert it into **string** with the help of **str()** method after getting our credentials.

  <h3 align="center">2nd Method </h3>

  - We have to install the following module:-

    ```bash
    pip install environ

    # or type this command
    pip3 install environ
    ```

  - **This module is used only in django framework only.**
  - In `settings.py` file 👇

    ```python
    import os
    from environ import Env

    # For Environment variable.
    env = Env()

    # To tell that our .env file in base directory.
    Env.read_env(os.path.join(BASE_DIR, ".env"))

    print(env("DATABASE_NAME"))
    print(env("DATABASE_PASSWORD"))
    ```

---

## How To Show Messages When User Logged In Or Log out :-

- When **User Logged In or Logged Out we can show message** with the help of **messages framework**.

  ### Adding a Message :-

  - Go To `views.py` file in your app directory and the following code
  - **Syntax :-** 👉 &nbsp;`messages.Tag(request,"Message Here")`
  - **This is shortcut method.**
  - `views.py` **file** 👇

    ```python
    from django.contrib.auth import authenticate, login
    from django.contrib import messages

    def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            # Here we show success message.
            messages.success(request, "Successfully Logged In.")

            return redirect("home")
        else:
             # Here we show  error message.
            messages.error(request, "There was an error UserName or Password.")

            return redirect("home")

    else:
        return render(request, "website/index.html")
    ```

    - **This is second method we can add message with this method also.**

    ```python
    from django.contrib import messages
    messages.add_message(request, messages.INFO, "Hello world.")
    ```

  ### Displaying Messages :-

  - In Our **templates** we add something like this :-
  - `index.html` **file** 👇

    ```html
    {% if messages %}
    <div class="messages">
      {% for message in messages %}

      <p class="{{ message.tags }}">{{ message }}</p>

      {% endfor %}
    </div>

    {% endif %}
    ```

  ### How To Customize Message tag :-

  - Go To your project `settings.py` file and add the following code :-
  - `settings.py` **file** 👇

    ```python
    from django.contrib.messages import constants as messages

    #  To change message constants
    MESSAGE_TAGS = {

            # messages.ERROR: "danger",
            # or we can add anything css class that we want.
            messages.ERROR: 'alert-danger',
            messages.DEBUG: 'alert-secondary',
            messages.INFO: 'alert-info',
            messages.SUCCESS: 'alert-success',
            messages.WARNING: 'alert-warning',


            }

    ```

- [Click Here](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#changing-the-minimum-recorded-level-per-request) for more information.

---

## How To configure Tailwind CSS with Django

<h3 align="center">1st Method</h3>

- After creating a **django project** **open your integrated terminal or terminal and go where** your `.venv` or `.gitignore` file is located and type the following commannd
- **This command will install Tailwind CSS as a dev dependency using NPM :-**

```bash
npm install -D tailwindcss
```

- Open `package.json` file
- **syntax :-** 👉&nbsp; **tailwindcss -i inputCSSPath -o outputCSSPath -w**

- **where** 👇

  - **-i** 👉 &nbsp; input
  - **-o** 👉 &nbsp; output
  - **-w** 👉 &nbsp; watch

  ```json

  "scripts":{
    "dev": "tailwindcss -i ./tailwind_practice/tailwindPractice/static/tw/tailwind-input.css -o ./tailwind_practice/tailwindPractice/static/css/output.css -w"
  }
  ```

- open your `input.css` file and write the following code:-

  ```css
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
  ```

- **Open the terminal where your package.json file is located and type the following command:-**

  ```bash
  npm run dev
  ```

- Next step, Using the Tailwind CLI create a new `tailwind.config.js` file:
  ```bash
  npx tailwindcss init
  ```
- Open `tailwind.config.js` file and write the following code :-

  ```javascript

  content: [
    // Syntax 👉 ./projectRootDirectory/**/*.{html,js}

    // This will write
      "./tailwind_practice/**/*.{html,js}"
    ],
  ```

- **Open static directory where you write your css in project root directory and create a folder css and inside css folder create a file which name output.css (or anything that you want css file).**
  - **path:-** 👉 **static/css/output.css**
- **This output.css file we will link or include in our base.html file.**
- Inside project root directory open `templates` type the follwing code:-

  - **path:-** 👉 **templates/base.html**

  ```html
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>{% block title %} Tailwind Practice {% endblock %}</title>

      <!-- Here we will link our output.css file -->
      <link rel="stylesheet" href="{% static 'css/output.css' %}" />
    </head>
    <body>
      <main
        class="min-h-screen flex flex-col items-center justify-center bg-[#333]"
      >
        {% block content %} {% endblock %}
      </main>
    </body>
  </html>
  ```

  - **path:-** 👉 **templates/pages/home.html**

  ```html
  {% extends 'base.html' %} {% block content %}
  <h1
    class="text-5xl px-2 py-4 text-black text-center bg-white rounded-lg w-2/3 hover:bg-orange-500 hover:cursor-pointer hover:text-white"
  >
    This is our Home Page.
  </h1>
  {% endblock %}
  ```

- **After doing above step run manage.py file in another terminal with the following command :-**
  ```bash
  python3 manage.py runserver
  ```

---

## How to handle media Files

- [Click Here](https://docs.djangoproject.com/en/5.0/topics/files/) for more information.

---

## ⭐ How To add Stripe Payment Gateway in project :-

- **After creating of stripe account get stripe `secret_key` and stripe `publish_key` from your stripe account.**
- There are 3 steps to do this task

1. **Create a Product and get product id [Click Here](https://docs.stripe.com/api/products/create?lang=python) For More Information.**
2. **Create Price and get price id [Click Here](https://docs.stripe.com/api/prices/create?lang=python) For More Information.**
3. **Create Checkout Session and get url [Click Here](https://docs.stripe.com/api/checkout/sessions?lang=python) For More Information.**

#### 🌟 For Multiple Products :-

- In `settings.py` file 👇

  ```python
  STRIPE_SECRET_KEY = 'Your_stripe_sec_key'
  STRIPE_PUB_KEY = 'Your_stripe_pub_key'
  ```

```python
import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY

proudcts = [
    {
      "product_name":"Watch",
      "price":1000,
      "quantity":1,
    }
]

def product_sales(products:list[dict]):

    line_items=[]
    for product in products:
        # create a product
        stripe_product_object = stripe.Product.create(name=product["product_name"])
        stripe_product_object_id=stripe_product_object.id

        # create price
        stripe_price_object = stripe.Price.create(
          currency="usd",
          unit_amount = product["price"]
          product = stripe_product_object_id
        )

        stripe_price_id = stripe_price_object.id
        line_items.append({
                "price":stripe_price_id,
                "quantity":product["quantity"]
        })
    
    base_end_point = "http://127.0.0.1:8000"
    success_url = f"{base_end_point}/purchase/start/"
    cancel_url = f"{base_end_point}/purchase/stop/"
    
    checkout_session = stripe.checkout.Session.create(
        line_items = line_items,
        mode = "payment",
        success_url = success_url,
        cancel_url = cancel_url
    )

    return checkout_session

  

```

#### 🌟 For Single Product :-
```python
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_KEY


def product_sales(product_name="Test Product", product_price=1000):
    stripe_prod_obj = stripe.Product.create(name=product_name)
    stripe_prod_obj_id = stripe_prod_obj.id

    stripe_price_obj = stripe.Price.create(
        currency="usd",
        unit_amount=product_price,
        product=stripe_prod_obj_id
    )

    stripe_price_id = stripe_price_obj.id

    base_end_point = "http://127.0.0.1:8000"
    success_url = f"{base_end_point}/purchase/start/"
    cancel_url = f"{base_end_point}/purchase/stop/"

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price": stripe_price_id,
                "quantity": 1
            }
        ],
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url
    )

    return checkout_session

```
