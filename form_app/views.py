from django.shortcuts import render
from form_app.forms import UserProfileInfoForm

def home(request):
    return render(request,'form_app/home.html')

def register(request):
    profile_form=UserProfileInfoForm()
    context={'profile_form':profile_form}
    return render(request,'form_app/register.html',context)

def save(request):
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(request.POST)
        if profile_form.is_valid():
            profile_form.save(commit=True)

    return render(request, 'form_app/save.html')

def login(request):
    return render(request,'form_app/login.html')

def profile(request):
    return render(request,'form_app/profile.html')
# Create your views here.
