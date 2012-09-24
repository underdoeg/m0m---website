# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import datetime

def index(request):
    c = RequestContext(request)
    return render_to_response('index.html', c)
    
