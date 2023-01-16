from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Faculty



class RegistrationForm(UserCreationForm):
    username=forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    department_name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = Faculty
        fields = ('username', 'age', 'email', 'id', 'gender', 'role','department_name','phone_number','password1','password2')
