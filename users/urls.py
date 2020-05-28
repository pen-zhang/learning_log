#\users\urls.py

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns= [
    # login page
    url(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'),
    
    # logout page
    url(r'^logout/$', views.logout_view,name='logout'),
    
    # register
    url(r'^register/$', views.register, name='register'),
        ]

