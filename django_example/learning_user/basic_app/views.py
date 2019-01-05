from django.shortcuts import render
from basic_app.forms import UserForm,UserprofileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        User_Form = UserForm(data=request.POST)
        UserprofileInfo_Form = UserprofileInfoForm(data=request.POST)

        if User_Form.is_valid() and UserprofileInfo_Form.is_valid():
            user = User_Form.save()
            user.set_password(user.password)
            user.save()

            profile = UserprofileInfo_Form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True

        else:
            print(User_Form.errors,UserprofileInfo_Form.errors)

    else:



        User_Form = UserForm()
        UserprofileInfo_Form = UserprofileInfoForm()

    return render(request, 'basic_app/registration.html', {'User_Form':User_Form, 'UserprofileInfo_Form':UserprofileInfo_Form,'registered':registered})


def User_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account is not active')
        else:
            print('someone tried to login and failed')
            print('user:{} and password {}'.format(username,password))
            return HttpResponse('invalid login details')

    else:
        return render(request, 'basic_app/login.html',{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def sepcial(request):

    return HttpResponse('you aRE logedin nice')
