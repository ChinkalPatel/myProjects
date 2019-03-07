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

from django.contrib import messages
from django.utils import timezone
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.dateparse import parse_date

from pysimplesoap.client import SoapClient
# Create your views here.

def home(request):
    client = SoapClient(wsdl='http://localhost:8080/BlogService?wsdl',trace=True)
    a=client.readBlogs(100)
    print("hello")
    print(a)
    return render_to_response("home.html")