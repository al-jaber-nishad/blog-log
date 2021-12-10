from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.decorators import decorators
import datetime



# Create your views here.

posts = [
  {
    'id': 1,
    'title': "First Post!",
    'author': 'nishad_updated',
    'content': "This is the first of this application.",
    'date_posted': datetime.time(10, 33, 45),
  },
  {
    'id': 2,
    'title': "Second Post!",
    'author': 'Nishad',
    'content': "This is the second of this application.",
    'date_posted': datetime.time(9, 33, 45),
  },
  {
    'id': 3,
    'title': "Third Post!",
    'author': 'Nishad',
    'content': "This is the second of this application.",
    'date_posted': datetime.time(8, 33, 45),
  },
  {
    'id': 4,
    'title': "Fourth Post!",
    'author': 'Nishad',
    'content': "This is the second of this application.",
    'date_posted': datetime.time(5, 33, 45),
  },
]

class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_name_object = 'posts'
  ordering = ['-date-posted']

class PostDetailView(DetailView):
  model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post 
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post 
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post 
  success_url = '/'
  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False


def home(request):
  
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'blog/home.html', context)