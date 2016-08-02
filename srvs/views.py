from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import time
# Create your views here.


def home(request):
    return render_to_response("home.html")

def error_handler(request):
    return render(request,"redirect.html")

@csrf_exempt
def calculation(request):
    START = time.time()
    print request.method
    if request.method == "POST":
        data = json.loads(request.body)
        number = int(data['number'])
        a,b = 0,1
        OUTPUT = 0
        
        if number<0:
            OUTPUT = "NUMBER IS NEGATIVE"
        elif number == 0:
            OUTPUT = 0
        elif number == 1:
            OUTPUT = 1
        else:
            for i in range(number-1):
                a,b= b,a+b
            OUTPUT=b
        
    print OUTPUT
    OUTPUT = str(OUTPUT)
    END = time.time()
    TIME = END-START
    return HttpResponse(json.dumps({"output":OUTPUT,"time":TIME}))
    