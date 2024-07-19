from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ['user_text','user_image']
        
        labels={
            "user_text":"Write Your Tweet :",
            "user_image":"Choose Your Image :"
        }
        widgets ={
            "user_text":forms.Textarea(
                attrs={
                    "placeholder":"Write Your Tweet Here...",
                    "class":"form-control input-field fs-4 text-white border border-3 border-white rounded-2",
                    "rows":"5",
                    "cols":"20",
            }),
            "user_image":forms.ClearableFileInput(
                attrs={
                    "class":"d-inline-block p-2 fs-5 fw-bold border-4",
                }
            )
        }
        
        
