from django.shortcuts import render

from log.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from log.models import UserProfileInfo
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request,'log/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'log/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'log/login.html', {})

def proshow(request):  
    user = User.objects.all()
    userprofileinfo = UserProfileInfo.objects.all()  
    return render(request,"proshow.html",{'user':user, 'userprofileinfo':userprofileinfo})

def profileshow(request, id):
    try:
        user = User.objects.get(id=id)
        userprofileinfo = UserProfileInfo.objects.get(user_id=id)  
        form = UserForm(request.POST, instance = user)
        if form.is_valid():  
            form.save()  
            return redirect("/proshow")
    except ObjectDoesNotExist:  
        # return HttpResponse("Exception: Data not found")
        return render(request, 'log/Error1.html', {})    
    return render(request, 'profileshow.html', {'user':user, 'userprofileinfo':userprofileinfo})
