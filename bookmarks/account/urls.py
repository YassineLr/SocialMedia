from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^register/$', view=views.register , name='register'),
    re_path(r'^logout/$', view=views.CostumLogoutView , name='logout'),
    re_path(r'^login/$', view=views.CustomLoginView.as_view(template_name='account/login.html'), name='login'),
    path('logged-out/', TemplateView.as_view(template_name='registration/logged_out.html'), name='logout_done'),
    re_path(r'^$', view=views.dashboard, name='dashboard'),
    re_path(r'^edit/$', view=views.edit, name='edit')
]
