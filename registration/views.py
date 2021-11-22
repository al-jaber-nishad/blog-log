from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"Account is created for {username}!")
      return redirect('home')
    else:
      messages.warning(request, "Fill the boxes carefully!")
  else:
    form = UserRegisterForm()
  return render(request, 'register.html', {'form':form})