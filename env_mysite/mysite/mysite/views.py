from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello world!")
#simply running the server does not display hello world
#URLconf is to be done to connect he url to the function
