from django.shortcuts import render,redirect,get_object_or_404
from .models import Save

def home(request) :
    messages = Save.objects
    return render(request,'home.html',{'messages':messages})

def submit(request) :
    s = Save()
    s.saving1 = request.GET['saving1']
    s.saving2 = request.GET['saving2']
    s.saving3 = request.GET['saving3']
    s.save()
    return redirect('/')

def detail(request,save_id) :
    message = get_object_or_404(Save, pk=save_id)
    return render(request,'detail.html',{'message':message})
    



