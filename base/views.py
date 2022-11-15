from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Suami, Istri, Penghulu, Akad, Wali

def akad_view(request):
    page = 'Akad'
    akadModels = Akad.objects.all()
    for wali in akadModels:
        print(wali.wali_set.all())
    context = {
        'akadList' : akadModels,
        'page' : page,
    }
    return render(request, 'base/akad.html', context)
    


