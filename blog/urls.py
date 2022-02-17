from django.urls import path 
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, Author

urlpatterns = [
  path('', views.home, name="home"),
  path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  path('posts/new/', PostCreateView.as_view(), name='post-create'),
  path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
  path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
  path('author/<int:pk>', views.Author, name='author'),
  
]