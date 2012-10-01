# Create your views here.
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from m0m.models import *

def index(request):
    t = loader.get_template('events.html')
    c = RequestContext(request, {
        'events': Event.objects.all()
    })
    return HttpResponse(t.render(c))