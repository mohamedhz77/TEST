from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreatedForm

@login_required
def image_create(request):
       if request.method=='POST':
              form=ImageCreatedForm(data=request.POST)
              if form.is_valid():
                     cd = form.cleaned_data
                     new_item=form.save(commit=False)
                     new_item.user=request.User
                     new_item.save()
                     messages.success(request,'Iamge added successfully')
                     return redirect('/')
       else:
              form=ImageCreatedForm(data=request.GET)
       return render(request,'image/create.html',{'form':form,'section':'images'})                     