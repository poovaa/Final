from django.shortcuts import render
from django.http import HttpResponse

def check(request):
	return render(request,"login.html")

def home(request):
	return render(request,"homepage.html")

def validate(request):
		return render(request,"donerlogin.html")


def validatee(request):
		return render(request,"login.html")









