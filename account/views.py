from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms  import  *
from .models import  *

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def UpdateUser(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(instance=request.user, data = request.POST)
        profile_form = UpdateProfileForm(instance=request.user.profile, data=request.POST, files = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'registration/update.html', {'user_form':user_form,'profile_form':profile_form })

@login_required
def user_list(request):
    users=User.objects.filter(is_active=True)
    return render(request,'user/list.html',{'users':users, 'section':'people'})  

@login_required
def user_detail(request,username):
    user=get_object_or_404(User,username=username, is_active=True)
    return render(request,'user/detail.html',{'user':user, 'section':'people'})  
