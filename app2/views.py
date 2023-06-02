from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_str(request):
    return HttpResponse('<h1>VIRAT IS GOOD BATSMAN</h1>')
def virat(request):
    return render(request,'rcb.html')
