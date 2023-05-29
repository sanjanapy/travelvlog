from django.http import HttpResponse
from django.shortcuts import render
from .models import add,place,blog
# Create your views here.
def create(request):
    var=add.objects.all()
    return render(request,"index.html",{'gives':var})


def fun(request):
    var=add.objects.all()
    make=blog.objects.all()
    obj=place.objects.all()
    context={'results':obj,'blogs':make,'gives':var

    }
    return render(request,"index.html",context)

def addition(request):
    num1 =int (request.GET["num1"])
    num2=int (request.GET["num2"])
    num3=num1+num2
    return render(request,"result.html",{"add":num3})