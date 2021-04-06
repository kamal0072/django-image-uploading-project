from django.shortcuts import render
from .forms import Userforms
from .models import UserImage


def home(request):
    if request.method=='POST':
        forms=Userforms(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
    else:
        forms=Userforms()
    myimg=UserImage.objects.all()
    return render(request,'library/home.html',{'form':forms,"img":myimg})

