from django.shortcuts import render
from testapp import models
from testapp.forms import UserForm, UserProfileInfoForm
#for login
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.
@login_required
def index(request):
    return render(request,'testapp/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse('you are login nice')


def register(request):

    registered = False

    if request.method == 'POST':

        user_from = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_from.is_valid() and profile_form.is_valid():
            user = user_from.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'Profile_pic' in request.FILES:
                profile.Profile_pic = request.FILES['Profile_pic']

            profile.save()

            registered = True

        else:
            print(user_from.errors,profile_form.errors)

    else:
        user_from = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'testapp/registration.html',
                            {'user_from':user_from,
                             'profile_form':profile_form,
                             'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account not active')


        else:
            print('someone tried to login and failed')
            print('username: {} and password:{}'.format(username,password))
            return HttpResponse('invalid login details supplied')

    else:
        return render(request, 'testapp/login.html',{})
