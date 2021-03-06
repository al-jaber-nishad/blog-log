from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Post
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

@login_required
def edit_profile(request, pk):
  if request.method == 'POST':
    # u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    if p_form.is_valid():
      # u_form.save()
      p_form.save()

      messages.success(request, 'You account has been updated!')
      return redirect('profile')
      
  else:
    # if pk:
    posts = Post.objects.filter(author_id=pk)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    
  context = {
    'p_form': p_form,
    'posts': posts,

  }
  return render(request, 'profile.html', context)


@login_required()
def profile(request):
  p_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'p_form': p_form
  }

  return render(request, 'profile.html', context)