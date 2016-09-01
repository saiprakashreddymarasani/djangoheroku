from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from employees.models import *
# Create your views here.
def home(request):
    return HttpResponse("hello")

def details(request):
    employees= Employee.objects.all()
    return render_to_response('naveed/details.html', {"employees": employees})

def employeedetails(request,id):
    employees= Employee.objects.get(pk=id)
    return render_to_response('naveed/employeedetails.html', {'employees': employees})

def add(request):
    if request.method=='GET':
        form= EmployeeForm()
        return render_to_response('naveed/add.html', {'form': form})
    elif request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.save()
        return HttpResponseRedirect('/details')
