from django.forms import ModelForm  
from .models import Post
from django import forms  
class FeedForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title','content']
        widgets ={ 
                   'title' : forms.TextInput(attrs={'type': 'text','class':' form-control,card-title','placeholder': 'Enter Title Here'}), 
                   'Content': forms.Textarea(attrs={'class': 'form-control card-text', 'placeholder': 'Enter content Here'}),

        }