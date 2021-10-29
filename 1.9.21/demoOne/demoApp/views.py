from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    # return HttpResponse("<h1>Hello World</h1>")
    # return render(request, 'home.html')
    return render(request, 'home.html', {'name':'Vaibhav'})

def add(request):

    val1 = request.POST['num1']
    val2 = request.POST['num2']
    try:
        res = int(val1) + int(val2)
    except:
         res = (val1) + (val2)

    return render(request, 'result.html', {'result':res})
    