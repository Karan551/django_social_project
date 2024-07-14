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