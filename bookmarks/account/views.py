from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from .forms import LoginForm, UserRegitrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView , LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Profile


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


def CostumLogoutView(request):
    logout(request)
    print(request)
    return redirect('logout_done')

def register(request):
    if request.method == 'POST':
        registerForm = UserRegitrationForm(request.POST)
        if registerForm.is_valid():
            new_user = registerForm.save(commit=False)
            new_user.set_password(registerForm.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            # print(new_user)
            return render (
                request,
                'registration/register_done.html',
                {'user_form': registerForm},
            )
    userForm = UserRegitrationForm()
    return render (
        request,
        'registration/register.html',
        {'user_form':userForm} 
    )

    

@login_required
def dashboard(request):
    return render(
                    request, 
                    'registration/dashboard.html', 
                    {'section':'dashboard'}
                )

@login_required
def edit(request):
    if request.method == 'POST':
        userForm = UserEditForm(
                                        instance=request.user, 
                                        data=request.POST
                                )
        profileForm = ProfileEditForm(
                                        instance=request.user.profile,
                                        data=request.POST,
                                        files=request.FILES
                                    )
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
    else:
        userForm = UserEditForm(instance=request.user)
        profileForm = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        'account/edit.html',
        {
            'user_form' : userForm,
            'profile_form' : profileForm
        }
    )

