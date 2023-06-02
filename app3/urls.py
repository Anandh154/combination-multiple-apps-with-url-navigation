from django.urls import path
from app3.views import *
app_name='app3'
urlpatterns=[
    path('app3_str/',app3_str,name='app3_str'),
    path('sachin/',sachin,name='sachin')
]