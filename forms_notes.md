#  Django Forms :-

### How To add Forms in Django App :- 
- Create a file in your  **django app** which name will be `forms.py`
- **Django forms syntax is similar to Django Model Fields.**
- **Creating a form in Django similar to the creating a Model in Django one thing we have to specify which fields would exist in the form what is the type.**
- Django field work like Django Model field and have following Syntax :-
  - **Syntax :-** 👉 &nbsp; `forms.fieldType(**kwargs)`
- **Path:-** 👉 &nbsp; **app/forms.py**

- **Syntax :-**
    ```txt
    from django import forms

    class FormName(forms.Form):
        # each field would be mapped input field in HTML
        field_name = forms.Field(**kwargs)
    ```

- **Example :-** 👉 &nbsp; **tweetApp/forms.py**
    - **Example:-** 👇 `forms.py`
    ```python
    from django import forms

    class RegisterForm(forms.Form):
        user_name = forms.CharField(max_length=100)

    ```
    - If we write the above code in forms then follwing html will be genertated 
    ```html
    <div>
         <!-- we can overwrite User name text with the help of label attribute. -->
        <label for="id_user_name">User name:</label>
        <input type="text" name="user_name" required="" id="id_user_name">
    </div>
    ```
- A field Have the follwing arguments :-
    1. &nbsp; **required -> bool**  `True` **(By default)**
    2. &nbsp; **label**
         - The **default label** for **a Field** is **generated from the field name by converting all underscores to spaces and upper-casing the first letter.** **Specify label if that default behavior doesn’t result in an appropriate (proper) label.**
    3. &nbsp; **help_text**
    4. &nbsp; **error_message**
         - The **error_messages** argument lets you override the **default messages** that the **field will raise**. **Pass in a dictionary with keys matching the error messages you want to override.**
    5. &nbsp; **disabled -> bool**
    6. &nbsp; **max_length** `None`**(Default)**
    7. &nbsp; **min_length** `None`**(Default)**
    8. &nbsp; **widget**
         - The **widget** argument lets you specify a **Widget class** to use when rendering the **Field**.
         - We can **attribute via widget argument**.

- [Click Here](https://docs.djangoproject.com/en/5.0/ref/forms/fields/) For More Information 

### How to add class or other attribute in HTML element via django forms :-

- Whenever we specify a **field** on **a form**, **Django** will use a **default widget** that is **appropriate** to the type of data that is to be displayed.
- However, if we want to use a **different widget** for a **field**, we can use the **widget argument** on the **field definition**.
- `widget=(attrs=None)` **(By Default)**
- **attrs :-** `attrs` is a **dictionary** **containing HTML attributes** to be set on the rendered widget.
  

```python
from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"my-name"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"size":"40"}))
    
    # we can also modify widget
    name.widget.attrs.update({"class":"special"})
    address.widget.attrs.update({"size":"125"})
```
- [Click Here](https://docs.djangoproject.com/en/5.0/ref/forms/widgets/) for more Information.

### How To add css classes on label element in django form :-


<h3 align="center">1st method</h3>


```html
<form class="bg-white rounded-3 px-3 py-2">
<h2>Contact Us:</h2>

{% for field in form %}
<label for="{{ field.auto_id }}" class="form-label fs-4 fw-bold">{{ field.label }}</label>

 {{ field }}

{% endfor %}
<button type="submit">Submit</button>
</form>

```

<h3 align="center">2nd method</h3>


```html

 <h1 class="mb-6 text-3xl text-center">Sign Up</h1>
<form action="." method="post">
{% csrf_token %}

<!-- {{form.as_p}} -->
<div class="mb-3">
    <label class="inline-block mb-2">UserName</label><br>
            
    <!-- this will create  an input field that type of text-->
    {{form.username}}
</div>

<div class="mb-3">
            
<label class="inline-block mb-2">Email</label><br>

<!-- this will create  an input field that type of email-->

{{form.email}}

</div>

<div class="mb-3">

    <label class="inline-block mb-2">Password</label><br>
            
<!-- this will create  an input field that type of password-->

    {{form.password1}}
</div>

<div class="mb-3">
    <label class="inline-block mb-2">Confirm Password</label><br>

    {{form.password2}}

</div>
        
{% if form.errors or form.non_field_errors %}
    <div class="mb-3 p-6 bg-red-100 hover:bg-teal-700 rounded-xl">

        {% for fields in form %}
            {{fields.errors}}
        {% endfor %}

        {{form.non_field_errors}}
    </div>

{% endif %}

    <button class="py-4 px-8 text-lg font-bold bg-teal-500 rounded-xl text-white hover:bg-teal-700">Submit</button>
    
</form>

```
-----
## Model Form :-
- If we are using database driven app , chances are are we’ll have forms that map closely to **Django models.** 
- In this case, it would be redundant(unnecessary) to define the field types in our form, because we’ve already defined the fields in our model.
- For this reason, Django provides a helper class that lets we create a **Form class from a Django model.**
- First create a file `forms.py` in your app.
  
- **path** 👉 `app/forms.py`
```python
from django.forms import ModelForm
from .models import Tweet

class TweetForm(ModelForm):
    class Meta:
        # Model That we will use.
        model = Tweet
        # fields that we want to use to create a form.
        fields = []

        # To use all fields
        #  fields = '__all__'
        
        # To exclude any field
        # exclude = ['cretated_at'] 

```
- if we are using all fields then we will write : <br/>  `fields = __all__` <br/>
- If we want to exclude any field then we will write :-<br/> `exclude = ["title"]`

- [Click Here](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/) For More Information. 

------

## How To Show Django Form in Templates (HTML) :-
- We don't need to much in our `index.html`(**any html file that we want to show our django form) template.**
- We have to provide a `<form></form>` **element and a submit button to submit that form.**
- **For example :-** 👇 `index.html`
  ```html
  <form method="post">
    {% csrf_token %}

    <!-- To show form  -->
    {{form}}

    <button type="submit">Submit</button>
  </form>

  ```
- All the **form’s fields** and **their attributes** will be **unpacked into HTML markup** from that `{{ form }}` by **Django’s template language.**
  #### Output Styles of a form :-
  - `as_div():-` 👉 &nbsp;**as_div()** renders the form as a series of `<div>` elements, with each `<div>` containing one field.
    - For example :-
    ```html
    <form method="post">
    {% csrf_token %}

    <!-- To show form  -->
    {{ form.as_div() }}

    <button type="submit">Submit</button>
    </form>
    ```  

  - `as_p():-` 👉 &nbsp;**as_p()** renders the form as a series of `<p>` tags, with each `<p>` containing one field.
  
  - `as_ul():-` 👉 &nbsp;**as_ul()** renders the form as a series of `<li>` tags, with each `<li>` containing **one field.** It does not include the `<ul>` or `</ul>`, so that you can specify any **HTML attributes** on the `<ul>` for flexibility.
  
  - `as_table():-` 👉 &nbsp;**as_table()** renders the form as an HTML `<table>`.
  
  - [Click Here](https://docs.djangoproject.com/en/5.0/ref/forms/api/#output-styles) For More Information.

----- 
## Looping Over the form's fields :-

- If we’re using the **same HTML for each of our form fields**, we can reduce duplicate code by **looping** through **each field** in turn using a `{% for %}` loop:
  ```html
  {%for field in form %}
  <div class="fieldWrapper">

    <!-- This will show form field errors -->
    {{field.errors}}

    <!--This will show lable tag  -->
    {{field.lable_tag}}

    <!-- This will show each field  -->
    {{field}}

  
  </div>
  {% endfor %}
  ```
- Some useful attributes are :-
    - `{{ field.errors }}` **:-** 👉 &nbsp;This contains any **validation errors** correspoding to that field. We can **customize the presentation of the errors** with a `{% for error in field.errors %}` **loop.**<br/> Here is an example **to show field errors :-** 👇
        ```html
        {% if form.errors or form.non_field_errors %}

            <div class="mb-3 p-6">
                {% for fields in form %}

                    {{fields.errors}}
                {% endfor %}

                {{form.non_field_errors}}

            </div>
        {% endif %}
        ```
    
    - `{{ field.label }}` **:-** 👉 &nbsp;This will show the **label** of the field.
    - `{{ field.label_tag }}` **:-** 👉 &nbsp;The field’s label wrapped in the appropriate HTML `<label>` tag. This includes the form’s **label_suffix.**  The **default** **label_suffix** is **a colon**.
    - [Click Here](https://docs.djangoproject.com/en/5.0/topics/forms/#looping-over-the-form-s-fields) For More Information.
     
--------

## Form API Important methods :-
- A Form instance is **either bound** a set of data , **or unbound.** 
  - If it’s **bound to a set of data**, it’s capable of **validating that data** and **rendering the form as HTML** with the data displayed in the HTML.
  - If **it’s unbound,** it **cannot do validation** **(because there’s no data to validate!)**, but **it can still render the blank form as HTML.**
  - **Simply We can say that A form that contains data is known as bound form and a form that contains no data or a blank form is called unbound form.**
   
    #### How To create an unbound Form :-
    -  To **create an unbound Form instance**, instantiate the class:
        ```python
        # Create an unbound form.
        form = TweetForm()
        ```
    #### How To bind data to a form :-
    - **To bind data to a form,** **pass the data as *a dictionary as the first parameter* to your Form class constructor:**
      ```python

       data = {
                "user_name" : "Mahesh",
                "user_text" : "Hello World !"
            }
        # Passing Data to a form.
        form = TweetForm(data)

      ``` 
    - In this **dictionary,** the **keys are the field names**, which correspond to the attributes in your Form class. **The values are the data you’re trying to validate.**
     
    #### How To Send Image or File via Form :-

    - Simlarly we can send text data to a server we can send Image or File to a server.
    - We will include, `request.FILES` **that holds data about FILES that submitted to the server.**
    - The form used to submit the file must have the `enctype="multipart/form-data"` **attribute included.**
    - The form should have a **method** value of **POST** and should have the `{% csrf_token %}` included as well.
    - **For Example :-** 👇 `index.html` file
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
         <meta charset="UTF-8">
        <title>Students Registartion</title>
        </head>
        <body>
        <form method = "post" enctype="multipart/form-data">
            {% csrf_token %}

            {{ form.as_p }}

            <button type="submit">Submit</button>
        </form>
        </body>
        </html>
        ``` 
    - In `views.py` 👇 file 
        ```python
        from django.shortcuts import render, redirect
        from .forms import StudentForm
  
        def avatarView(request):
        
            if request.method == 'POST':
            # Here we will write first text data and second image or binary data.
                form = StudentForm(request.POST, request.FILES)
        
                if form.is_valid():
                    # To save that form.
                    form.save()
                    return redirect('success')
            else:
                form = StudentForm()
            return render(request, 'studentform.html', {'form' : form})

        ``` 
    - [Click Here](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/) For More Information.
- 


- `form.is_bound` **:-** 👉&nbsp; It is used to check form is bound or unbound instances at runtime.
  
- `form.is_valid()` **:-** 👉&nbsp; **It is used to validate a bound Form , this returns a boolean value.**
    ```python
    data = {
                "user_name" : "Mahesh",
                "user_text" : "Hello World !"
            }
        # Passing Data to a form.
        form = TweetForm(data)

        # To validate a bound form
        form.is_valid()
    ```


- `form.save()` **:-** 👉&nbsp; It is used **to save data** in a database.
- `form.delete()` **:-** 👉&nbsp; It is used **to delete data** in a database.
- `form.errors` **:-** 👉&nbsp; **This returns a dictionary of error messages.** In that dictionary, the **keys** are the **field names**, and the **values are lists of strings representing the error messages.** **The error messages are stored in lists because a field can have multiple error messages.**
- `form.non_field_errors()` **:-** 👉&nbsp; **This method returns the list of errors from Form.errors that aren’t associated with a particular field.** 

- [Click Here](https://docs.djangoproject.com/en/5.0/ref/forms/api/#django.forms.Form.errors) For More Inforation.