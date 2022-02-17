from django.shortcuts import render, get_object_or_404
from .models import Post
from registration.models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# from django.contrib.decorators import decorators
import datetime
from django.core.paginator import Paginator

def home(request):
  posts = Post.objects.all()
  paginator = Paginator(posts, 5)

  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)


def Author(request, pk):
  posts = Post.objects.filter(author_id=pk)

  author = Profile.objects.get(user=pk)

  context = {
    'posts': posts,
    'author': author,
  }

  return render(request, 'blog/author.html', context)
  

def Search(request):
  if request.method == "GET":
    query = request.GET.get('query', 'nothing')

    if query:
      posts = Post.objects.filter(content__icontains=query)
    else:
      posts = {'ddd'}

  context = {
    'posts': posts,
  }

  return render(request, 'blog/search-page.html', context)



class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ['date_posted']
  paginate_by = 5

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
  model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post 
  fields = ['title', 'content', 'thumbnail_image']

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
