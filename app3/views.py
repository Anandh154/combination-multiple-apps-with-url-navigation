from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app3_str(request):
    return HttpResponse('<h1>SACHIN TENDULKAR IS GOOD BATSMAN</h1>')
def sachin(request):
    return render(request,'mi.html')

