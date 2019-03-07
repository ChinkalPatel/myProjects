from django.shortcuts import  get_object_or_404,render

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
from employee.models import *
from django.contrib import messages
from django.utils import timezone
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText

def profile(request):
    if request.session.get('unm') is not None:
        c1={}
        c1.update(csrf(request))
        s=Employee.objects.get(employee_name = request.session.get('unm'))
        print(s)
        c1['p']=s
        return render_to_response('Employee.html',c1)
    else:
        return HttpResponseRedirect('/admission/home/')

def complainshow(request):
    data=Complain.objects.all()
    com={"complains":data}
    return render_to_response('Complainshow.html',com)

def changestatus(request):
    q1=int('0' + request.GET.get('q',''))
    if q1 is not None:
        obj=Complain.objects.get(complain_id=q1)
        obj.status="done"
        obj.save()
    return HttpResponseRedirect("/employee/complainshow")

def gatepass(request):
    dt=date.today()
    print(dt)
    data=Gatepass.objects.all()
    g={"gatepasses":data,'dt':dt}
    return render_to_response('GatepassAllow.html',g)

def gatepassallow(request):
    q1=int('0' + request.GET.get('q',''))
    if q1 is not None:
        obj=Gatepass.objects.get(gatepassid=q1)
        obj.cheak="check"
        obj.save()
    return HttpResponseRedirect("/employee/gatepass/")

@property
def is_past_due(self):
    print("hello")
    return True

def showcanteenitem(request):
    c1={}
    c1.update(csrf(request))
    data=Canteen.objects.all()
    i={"items":data, "c1":c1}
    return render(request,'CanteenDetailAdd.html',i)

def removecanteenitem(request):
    q1=int('0' + request.GET.get('q',''))
    if q1 is not None:
        obj=Canteen.objects.get(itemid=q1)
        obj.delete()
    return HttpResponseRedirect("/employee/showcanteenitem")



def addcanteenitem(request):
    itemid = request.POST.get('itemid','')
    name= request.POST.get('itemname','')
    price = request.POST.get('itemprice','')
    myfile = request.FILES.get('myfile')
    print(myfile)
    c = Canteen(itemid=itemid, itemname = name, itemprice=price, image=myfile)
    c.save()
    return HttpResponseRedirect("/employee/showcanteenitem/")

def updatecanteenitem(request):
    q1=int('0' + request.GET.get('q',''))
    print(q1)
    if q1 is not None:
        name= request.POST.get('itemname','')
        price = request.POST.get('itemprice','')
        myfile = request.FILES.get('myfile')
        obj=Canteen.objects.get(itemid=q1)
        obj.itemname=name
        obj.itemprice=price
        obj.image=myfile
        obj.save()
        return HttpResponseRedirect("/employee/showcanteenitem")
    else:
        return HttpResponseRedirect("/employee/profile/")

def messdetail(request):
    c1={}
    c1.update(csrf(request))
    s=WeekMenu.objects.all()
    print(s)
    c1['p']=s
    return render_to_response('MessDetailAdd.html',c1)

def messdetailadd(request):
    q1=request.GET.get('day','')
    print('hello'+ q1)
    if q1 is not None:
        breakfast = request.POST.get('breakfast','')
        lunch = request.POST.get('lunch','')
        dinner = request.POST.get('dinner','')
        obj=WeekMenu.objects.get(day=q1)
        obj.breakfast=breakfast
        obj.lunch=lunch
        obj.dinner=dinner
        obj.save()
        return HttpResponseRedirect("/employee/messdetail/")
    else:
        return HttpResponseRedirect("/employee/messdetail/")

def electricitybill(request):
    c1={}
    c1.update(csrf(request))
    return render_to_response('electricitybill.html',c1)
    

def electricitybillsend(request):
    sid=request.POST.get('sid','')
    units=int('0' + request.POST.get('nunit'))-int('0'+request.POST.get('lunit'))
    price=int('0' + request.POST.get('price'))
    month=request.POST.get('month','')
    tprice=price*units
    
    FROM_EMAIL="sdproyal99@gmail.com"
    PASSWORD="chinkal99"
    
    try:
        gmail = smtplib.SMTP('smtp.gmail.com',587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(FROM_EMAIL,PASSWORD)
    except:
        print("Couldn't setup email!!")

    msg=MIMEText(tprice)

    msg['Subject']='electricitybill'

    msg['To']='chinkalpatel1998@gmail.com'

    msg['From']=FROM_EMAIL

    try:
        gmail.send_message(msg)

    except:
        print("COULDN'T SEND EMAIL")
    
    obj=Electricitybill(units=units,unit_price=price,month=month,studentid=sid,totalprice=tprice)
    obj.save()
    return HttpResponseRedirect("/employee/electricitybill/")


def logout(request):
    if request.session.get('unm') is not None:
        del request.session['unm']
        del request.session['pass']
        auth.logout(request)
        return HttpResponseRedirect('/admission/home')
    else:
        return HttpResponseRedirect('/admission/login')

def changepassword(request):
    c1={}
    c1.update(csrf(request))
    return render_to_response('EmployeeChangepassword.html',c1)

def changepassworddone(request):
    Old_Password = request.POST.get('Old_Password','')
    if Old_Password==request.session.get('pass'):
        New_Password = request.POST.get('New_Password','')
        Confirm_Password = request.POST.get('Confirm_Password','')
        if New_Password==Confirm_Password:
            u = User.objects.get(username = request.session.get('unm'))
            u.set_password(New_Password)
            u.save()
            request.session["pass"]=New_Password
            return HttpResponseRedirect('/employee/profile/')
        else:
            return HttpResponseRedirect('/employee/changepassword/')
    else:
        return HttpResponseRedirect('/emplyoee/changepassword/')
# Create your views here.

