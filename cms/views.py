# content of view.py
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from cms.models import *

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def login(request):
    return render_to_response("login.html",locals())
def dashboard(request):
    return render_to_response("dashboard.html",locals())
                       