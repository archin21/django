from django.shortcuts import render
from app_5_g.forms import profile_forms,user_forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect

def fun1(request):
    return render(request,'app/index.html',)
def fun2(request):
    registered=False
    if request.method=='POST':
        f1=user_forms(data=request.POST)
        f2=profile_forms(data=request.POST)
        if f1.is_valid() and f2.is_valid():
            user=f1.save()
            user.set_password(user.password)
            user.save()

            profile=f2.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True
        else:
            return (f1.errors,f2.errors)
    else:
        f1=user_forms()
        f2=profile_forms()
    return render(request,'app/registeration.html',context=
    {'f1':f1,'f2':f2,'registered':registered})
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('account inactive')
        else:
            return HttpResponse('wrong details')
    else:
        return render(request,'app/login.html',)
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))   

# Create your views here.
