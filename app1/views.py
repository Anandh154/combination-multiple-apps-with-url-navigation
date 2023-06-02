from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1_str(request):
    return HttpResponse('<h1>DHONI IS A GOOD BATSMAN AND WIICKETKEEPER</h1>')
def dhoni(request):
    return render(request,'csk.html')