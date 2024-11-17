from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^register/$', view=views.register , name='register'),
    re_path(r'^logouts/$', view=views.CostumLogoutView , name='logout'),
    re_path(r'^login/$', view=views.CustomLoginView.as_view(template_name='account/login.html'), name='login'),
    re_path(r'^$', view=views.dashboard, name='dashboard')
]
