from django.shortcuts import render
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
from student.models import *
from django.contrib import messages
from django.utils import timezone
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.dateparse import parse_date

# Create your views here.
def profile(request):
    if request.session.get('unm') is not None:
        c1={}
        c1.update(csrf(request))
        s=Student.objects.get(student_fname = request.session.get('unm'),password = request.session.get('pass'))
        print(s)
        c1['p']=s
        return render(request,'Profile.html',c1)
    else:
        return HttpResponseRedirect('/admission/home/')

def canteen(request):
    data=Canteen.objects.all()
    i={"items":data}
    return render(request,'Canteen.html',i)

def changepassword(request):
    c1={}
    c1.update(csrf(request))
    return render(request,'Changepassword.html',c1)

def changepassworddone(request):
    Old_Password = request.POST.get('Old_Password','')
    if Old_Password==request.session.get('pass'):
        New_Password = request.POST.get('New_Password','')
        Confirm_Password = request.POST.get('Confirm_Password','')
        if New_Password==Confirm_Password:
            s=Student.objects.get(studentid = request.session.get('unm'),password = request.session.get('pass'))
            s.password=New_Password
            s.save()
            u = User.objects.get(username = request.session.get('unm'))
            u.set_password(New_Password)
            u.save()
            request.session["pass"]=New_Password
            return HttpResponseRedirect('/student/profile')
        else:
            return HttpResponseRedirect('/student/changepassword')
    else:
        return HttpResponseRedirect('/student/changepassword')
def complain(request):
    c1={}
    c1.update(csrf(request))
    return render(request,'Complain.html',c1)

def complainregister(request):
    complain = request.POST.get('complain','')
    myfile = request.FILES.get('myfile')
    print(myfile)
    c = Complain(reason= complain, date=datetime.datetime.today().date(), status="false", student_studentid=request.session['unm'],proof=myfile)
    c.save()
    return HttpResponseRedirect('/student/profile')

    
def gatepass(request):
    c1={}
    c1.update(csrf(request))
    return render(request,'Gatepass.html',c1)


def gatepassregister(request):
    place = request.POST.get('place','')
    sdate = request.POST.get('sdate')
    ddate = request.POST.get('ddate')
    print(datetime.date.today())
    
    if ddate < sdate or parse_date(sdate) < datetime.date.today():
        return HttpResponseRedirect('/student/gatepass/')
    else:
        c = Gatepass(studentid=request.session['unm'], place = place, sdate=sdate, ddate=ddate,cheak='uncheck')
        c.save()
        return HttpResponseRedirect('/student/profile')
    

def mess(request):
    c1={}
    c1.update(csrf(request))
    s=WeekMenu.objects.all()
    print(s)
    c1['p']=s
    return render(request,'Mess.html',c1)


def electricity(request):
    c1={}
    c1.update(csrf(request))
    s=Electricitybill.objects.get(studentid=request.session.get('unm'),payment_status="pending")
    print(s)
    c1['p']=s
    return render(request,'electricity.html',c1)

def logout(request):
    if request.session.get('unm') is not None:
        del request.session['unm']
        del request.session['pass']
        auth.logout(request)
        return HttpResponseRedirect('/admission/home')
    else:
        return HttpResponseRedirect('/admission/login')
