from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StuForm
from .models import Student

def home(request):
    if request.method == "POST":
        data = StuForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("about")
    myform=StuForm()
    return render(request,"web.html",{'form':myform})
def about(request):
    return render(request,'index.html')



def fun(request):
    obj=Student.objects.all()
    return render(request,'index.html',{'data':obj})

def register(request):
    if request.method=='POST':
        data=StuForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("fun")
        return redirect("update")
    myform=StuForm()
    return render(request,'update.html',{'form':myform})
def delete(request,id):
    obj=Student.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect("fun")
    return render(request,'delete.html')









