from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views


app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name = 'register'),
    path('logout/', LogoutView.as_view(template_name='logged_out.html'), name='logout'),
]
