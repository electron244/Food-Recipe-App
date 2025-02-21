from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method =="POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        print(f"This is Title {title}")
        print(f"This is Text {text}")
        Recipe.objects.create(title=title,text=text)
        return redirect("/")
    
    data = Recipe.objects.all()
    return render(request,'index.html',{"data":data})

def delete(request,id):
    data = Recipe.objects.get(id = id)
    data.delete()
    return redirect('/')


def update(request,id):
    if request.method =="POST":
        update = Recipe.objects.get(id=id)
        title = request.POST.get("title")
        text = request.POST.get("text")
        print(update,title,text)
    return render(request,'update.html',{"update":update})
    