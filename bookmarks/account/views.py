from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy


# Create your views here.

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     # return HttpResponse('Authentificated successfully')
#                 else :
#                     return HttpResponse('Disabled account')
#             else :
#                 return HttpResponse('invalid login')
#     else :
#         form = LoginForm()
#     return render(request, 'account/login.html',{'form':form})


# def user_logout(request):
#     pass

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        # if self.request.user.is_authenticated:
        #     return redirect(reverse_lazy('dashboard'))
        return super().dispatch(request, *args, **kwargs)


# @login_required
def dashboard(request):
    return render(
                    request, 
                    'registration/dashboard.html', 
                    {'section':'dashboard'}
                )