from django.shortcuts import render,redirect
from form_app.forms import UserProfileInfoForm, UserForm

from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import  login_required

from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth.models import User
from form_app.models import UserProfileInfo


def home(request):
    return render(request, 'form_app/home.html')


def register(request):
    profile_form = UserProfileInfoForm()
    user_form = UserForm()
    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'form_app/register.html', context)


def save(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if profile_form.is_valid() and user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user


            if 'profile_pic' in request.FILES :
                profile.profile_pic = request['profile_pic']
            profile.save()

    return render(request, 'form_app/save.html')


def user_login(request):
    return render(request, 'form_app/login.html')


def profile(request):
    username = password = ''
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['password']
        print(username+' password '+password)

        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_active :
                login(request,user)
                #
                a=User.objects.get(username=username)
                b=UserProfileInfo.objects.get(user=a.id)
                print(b)
                context = { 'user' : a,'profile' : b}
                return render(request,'form_app/profile.html',context)
            else:
                return HttpResponse('user is not active')
        else:
            return HttpResponse('Invalid details')
    else:
        return render(request,'form_app/login.html')

@login_required
def user_logout(request):
    # a = User.objects.get(username=username)
    logout(request)
    return render(request, 'form_app/home.html')

# Create your views here.
