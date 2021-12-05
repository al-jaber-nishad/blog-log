from django.shortcuts import render
# from django.contrib.decorators import decorators

# Create your views here.

posts = [
  {
    'title': "First Post!",
    'description': "This is the first of this application.",
  },
  {
    'title': "Second Post!",
    'description': "This is the second of this application.",
  }
]


def home(request):
  context = {
    'posts': posts,
  }
  return render(request, 'home.html', context)