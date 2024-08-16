from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Tweet


class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ["user_text", "user_image"]

        labels = {
            "user_text": "Write Your Tweet :",
            "user_image": "Choose Your Image :",
        }
        widgets = {
            "user_text": forms.Textarea(
                attrs={
                    "placeholder": "Write Your Tweet Here...",
                    "class": "form-control input-field fs-4 text-white border border-2 border-info rounded-2 mb-3",
                    "rows": "5",
                    "cols": "20",
                }
            ),
            "user_image": forms.FileInput(
                attrs={
                    "class": "d-inline-block px-3 py-2 fs-5 fw-bold border-2 rounded-2",
                    "accept":".png, .jpeg, .jpg"
                }
            ),
        }


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Your user name:",
                "class": "px-3 py-2 fs-4 d-block mb-4 rounded-2 w-100",
            }
        ),
    )

    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter Your Email:....",
                "class": "px-3 py-2 fs-4 d-block mb-4 w-100 rounded-2",
                "autocomplete": "username",
            }
        ),
    )

    password1 = forms.CharField(
        label="Enter Your Password:-",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Your Password ...",
                "class": "px-3 py-2 fs-4 d-block mb-4 w-100 rounded-2",
                "autocomplete": "new-password",
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirm Your Password:-",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Your Password ...",
                "class": "px-3 py-2 fs-4 d-block mb-2 w-100 rounded-2",
                "autocomplete": "new-password",
            }
        ),
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Enter Your UserName:",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Your UserName...",
                "class": "px-3 py-2 fs-4 d-block mb-4 w-100 rounded-2",
                "autocomplete":"username"
            }
        ),
    )

    password = forms.CharField(
        label="Enter Your Password:",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Your Password...",
                "class": "px-3 py-2 fs-4 d-block mb-4 w-100 rounded-2",
                "autocomplete":"current-password",
            }
        ),
    )

