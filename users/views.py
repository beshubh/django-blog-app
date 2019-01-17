from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        print('sk0')
        if form.is_valid():
            form.save()
            print('sk')
            username=form.cleaned_data.get('username') 
            messages.success(request,f'Your account has been created and you can now login')
            print('sk1')
            return redirect('login')   
    else: 
        print('sk2')
        form=UserRegisterForm()
    return render(request,'users/register.html',{"form":form})
@login_required
def profile(request):
    if request.method == "POST":
        u_update=UserUpdateForm(request.POST, instance=request.user)
        p_update=ProfileUpdateForm(request.POST,request.FILES ,instance=request.user.profile)
        if u_update.is_valid() and p_update.is_valid:
            u_update.save()
            p_update.save()
            messages.success(request,f'Your account has been updated! ')
            return redirect('profile')

    else:
        u_update=UserUpdateForm(instance=request.user)
        p_update=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_update':u_update,
        'p_update':p_update
    }
    return render(request,'users/profile.html',context)

