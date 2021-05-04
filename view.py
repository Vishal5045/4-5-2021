from django.http import Httpresponce
from django.shortcuts import render

def myweb(request):
    return render(request,"one.html")
    