from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^login/$', view=views.CustomLoginView.as_view(template_name='account/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^$', view=views.dashboard, name='dashboard')
]
