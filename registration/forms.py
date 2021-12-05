from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Userame")
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="First Name")
  last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Last Name")
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label="Email")
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Password")
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Password Confirmation")


  class Meta:
    model = User

    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

