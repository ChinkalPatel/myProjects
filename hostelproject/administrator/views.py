from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.template import RequestContext
from django.db import IntegrityError
from administrator.models import *
from django.contrib import messages

def index1(request):
    if request.session.get('unm') is not None:
        c1={}
        c1.update(csrf(request))
        s=Admin.objects.get(lname = request.session.get('unm'))
        print(request.session.get('profile'))
        print(s)
        c1['p']=s
        return render(request,'index1.html',c1)
    else:
        return HttpResponseRedirect('/admission/home/')
    
def updateadmin(request):

    c = Admin.objects.get(lname = request.session.get('unm'))
    c.fname= request.POST.get('fname','')
    c.mname = request.POST.get('mname','')
    c.email = request.POST.get('email','')
    c.gender= request.POST.get('gender','')
    c.city = request.POST.get('city','')
    c.address= request.POST.get('address','')
    c.profile = request.FILES.get('myfile')
    c.save()
    return HttpResponseRedirect('/administrator/index1/')

def employee1(request):
    c1={}
    c1.update(csrf(request))
    s=Employee.objects.all()
    print(s)
    c1['p']=s
    return render(request,'employee1.html',c1)

def employee1remove(request):
    q1=int('0' + request.GET.get('q',''))
    if q1 is not None:
        obj=Employee.objects.get(employeeid=q1)
        obj.delete()
    return HttpResponseRedirect("/administrator/employee1/")

def employee1add(request):
    name= request.POST.get('name','')
    dob = request.POST.get('dob','')
    contact_no = request.POST.get('contact_no','')
    aadhar_no = request.POST.get('aadhar_no','')
    job_assigned= request.POST.get('job_assigned','')
    join_date = request.POST.get('join_date','')
    gender= request.POST.get('gender','')
    salary = request.POST.get('salary','')
    
    c = Employee(employee_name=name,dob=dob,contact_no=contact_no,aadhar_no=aadhar_no,job_assigned=job_assigned,join_date=join_date,gender=gender,salary=salary)
    c.save()
    return HttpResponseRedirect("/administrator/employee1/")

def student(request):
    data=Student.objects.all()
    i={"items":data}
    return render(request,'Student.html',i)
    
def studentremove(request):
    q1=int('0' + request.GET.get('q',''))
    if q1 is not None:
        obj=Student.objects.get(studentid=q1)
        
        obj1=User.objects.get(username=obj.student_fname)
        obj.delete()
        obj1.delete()
    return HttpResponseRedirect("/administrator/student/")


def changepassword1(request):
    c1={}
    c1.update(csrf(request))
    return render_to_response('Changepassword1.html',c1)

def changepassworddone1(request):
    Old_Password = request.POST.get('Old_Password','')
    if Old_Password==request.session.get('pass'):
        New_Password = request.POST.get('New_Password','')
        Confirm_Password = request.POST.get('Confirm_Password','')
        if New_Password==Confirm_Password:
            u = User.objects.get(username = request.session.get('unm'))
            u.set_password(New_Password)
            u.save()
            request.session["pass"]=New_Password
            return HttpResponseRedirect('/administrator/index1/')
        else:
            return HttpResponseRedirect('/administrator/changepassword1')
    else:
        return HttpResponseRedirect('/administrator/changepassword1')

def signout(request):
    if request.session.get('unm') is not None:
        del request.session['unm']
        del request.session['pass']
        auth.logout(request)
        return HttpResponseRedirect('/admission/home')
    else:
        return HttpResponseRedirect('/admission/login')