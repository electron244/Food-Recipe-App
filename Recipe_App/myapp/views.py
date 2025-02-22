from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method =="POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        Recipe.objects.create(title=title,text=text)
        return redirect("/")
    
    data = Recipe.objects.all()
    return render(request,'index.html',{"data":data})

def delete(request,id):
    data = Recipe.objects.get(id = id)
    data.delete()
    return redirect('/')


def update(request,id):
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        Recipe.objects.filter(id=id).update(title=request.POST.get("title"),text=request.POST.get("text"))
        return redirect('/')
        # title = request.POST.get("title")
        # text = request.POST.get("text")
        # recipe.title = title
        # recipe.text = text
        # recipe.save()
        # return redirect('/')

    context = {"recipe":recipe}
    return render(request,'update.html',context)

