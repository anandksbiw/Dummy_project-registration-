from django.shortcuts import render, redirect
from form_app.forms import UserProfileInfoForm, UserForm, UploadForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from form_app.models import UserProfileInfo, librarydue


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
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
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
        # print(username + ' password ' + password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #
                a = User.objects.get(username=username)
                b = UserProfileInfo.objects.get(user=a.id)
                # print(b)
                context = {'user': a, 'profile': b}
                return render(request, 'form_app/profile.html', context)
            else:
                return HttpResponse('user is not active')
        else:
            return HttpResponse('Invalid details')
    else:
        return render(request, 'form_app/login.html')






@login_required
def user_logout(request):
    # a = User.objects.get(username=username)
    logout(request)
    return render(request, 'form_app/home.html')


# Create your views here.

def librarian(request):
    upload_form = UploadForm()
    context = {'upload': upload_form}
    return render(request, 'form_app/librarian.html', context)


def uploaded(request):
    import openpyxl

    if request.method == "POST":
        path = request.FILES['file']

    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active

    cell_obj = sheet_obj.cell(row=2, column=2)

    print(cell_obj.value)

    # book_resource = resources.modelresource_factory(model=librarydue)()
    # dataset = Dataset(['', 'static/library.ods'], headers=['roll', 'due'])
    # result = book_resource.import_data(dataset, dry_run=True)
    # print(result.has_errors())
    # result = book_resource.import_data(dataset, dry_run=False)
    # return render(request, 'form_app/home.html')
    # # if request.method == 'POST':
    # # person_resource = LibraryResource()
    # # dataset = Dataset()
    # # new_roll = request.FILES['file']
    # # dataset.load(open(request.FILES['file']).read())
    # # result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
    # # if not result.has_errors():
    # #     person_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'form_app/home.html')
