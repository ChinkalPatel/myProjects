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
from admission.models import *
from django.contrib import messages

from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText

def index(request):
    request.session['cno']=0
    request.session['gno']=0
    return render_to_response('index.html')

def signup(request):
    c1={}
    c1.update(csrf(request))
    return render_to_response('Admission.html',c1)

def sign(request):
    
    student_fname = request.POST.get('fname', '')
    student_mname= request.POST.get('mname', '')
    student_lname = request.POST.get('lname', '')
    email=request.POST.get('email','')
    password1 = student_fname
    dob = request.POST.get('bdate', '')
    

    secret_key = b'1234567890123467890'
    u = User(username = student_fname)
    u.set_password(password1)
    u.save()
    
    
    student = Student(student_fname = student_fname, password = password1, student_mname = student_mname, student_lname = student_lname,dob = dob,email=email)
    student.save()
    
    FROM_EMAIL="sdproyal99@gmail.com"
    PASSWORD="chinkal99"
    
    try:
        gmail = smtplib.SMTP('smtp.gmail.com',587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(FROM_EMAIL,PASSWORD)
    except:
        print("Couldn't setup email!!")

    msg=MIMEText(password1)

    msg['Subject']='password'

    msg['To']=email

    msg['From']=FROM_EMAIL

    try:
        gmail.send_message(msg)

    except:
        print("COULDN'T SEND EMAIL")

    return HttpResponseRedirect('/admission/login/')



def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('Login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    q1=request.GET.get('cat','')
    print(q1)
    if q1 is not None:
        user = auth.authenticate(username = username, password = password)
        request.session["unm"]=username
        request.session["pass"]=password
        if user is not None:
            if q1=="admin":
                if user.is_superuser==1 and user.is_staff==1:
                    auth.login(request, user)
                    s=Admin.objects.get(lname = request.session.get('unm'))
                    request.session['profile']=s.profile
                    return HttpResponseRedirect('/administrator/index1/')
            if q1=="student":
                if user.is_superuser==0 and user.is_staff==0:
                    auth.login(request, user)
                    return HttpResponseRedirect('/student/profile/')
            if q1=="employee":
                if user.is_superuser==0 and user.is_staff==1:
                    auth.login(request, user)
                    return HttpResponseRedirect('/employee/profile/')
        else:
            return HttpResponseRedirect('/admission/login/')
    else:
        return HttpResponseRedirect('/admission/home/')


def contact(request):
    return render_to_response('contact.html')

def about(request):
    return render_to_response('about.html')

def gallery(request):
    return render_to_response('gallery.html')
