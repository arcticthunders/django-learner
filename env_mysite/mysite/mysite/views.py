from django.http import HttpResponse
import datetime as dt
from django import template as tp


def hello(request):
    return HttpResponse("hello world!")
#simply running the server does not display hello world
#URLconf is to be done to connect he url to the function

def current_datetime(request):
    now = dt.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, hours):
    try:
        hours = int(hours)
    except ValueError:
        raise Http404()
    time = dt.datetime.now() + dt.timedelta(hours = hours)
    html = "<html><body>It %s hours it will be %s.</body></html>" % (hours, time)
    return HttpResponse(html)

def printName(request, name):
    try:
        name = str(name)
    except ValueError
        raise Http404()
    t = tp.Template('My name is {{name}}')
    c = tp.context({'name':name})
    returnString = t.render(c)
    return(returnString)
