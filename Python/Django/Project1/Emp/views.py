from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.http import HttpResponse

# Importing model
from Emp.models import emp

# Create your views here.
def show_list(request):
    list = emp.objects.all()
    data = {'emp_list':list}
    return render(request,'emp_list.html',context=data)
##

def add(request):
    return render(request,'add.html')
##

def new(request):
    x = request.POST['eid']
    y = request.POST['ename']
    emp1 = emp(eid=x, ename=y)
    emp1.save()
    
    list = emp.objects.all()
    
    data = {'emp_list':list}
    return render(request,'emp_list.html',context=data)
## 
   
def update(request):
    id = request.POST['eid']
    id = int(id)-1
    list = emp.objects.all()[id]
    list.ename = request.POST['ename']
    list.save()
    list1 = emp.objects.all()
    return HttpResponse('Record Updated')

def delete(request):
    id = request.POST['eid']
    id = int(id)-1
    list = emp.objects.all()[id]
    list.delete()
    return HttpResponse('Record Deleted')