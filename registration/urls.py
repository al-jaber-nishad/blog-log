from django.urls import path 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views 


urlpatterns = [
  path('register/', views.register, name="register"),
  path('profile/', views.profile, name='profile'),
  path('edit-profile/<int:pk>', views.edit_profile, name="edit-profile"),
  path('login/', auth_views.LoginView.as_view(), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)