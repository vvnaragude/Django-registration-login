from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Registrtion


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autofocus': 'autofocus'})

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']









class RegistrtionForm(forms.ModelForm):
    class Meta:
        model = Registrtion
        fields = '__all__'
        
        
