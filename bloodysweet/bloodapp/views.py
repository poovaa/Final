from django.shortcuts import render
from.models import Donor

# Create your views here.

def adddoner(request):
	ndoner=request.POST.get('name')
	bank=request.POST.get('bloodbank')
	dis=request.POST.get('district')
	num=request.POST.get('number')
	email=request.POST.get('email')
	pas=request.POST.get('password')
	bg=request.POST.get('bloodgroup')
	record=Donor(name=ndoner,bloodbank=bank,district=dis,number=num,email=email,password=pas,bloodgroup=bg)
	record.save()
	return render(request,'reg.html')

def cblood(request):
	sdistrict=request.POST.get('district')
	bl=request.POST.get('blood-group')
	r=Donor.objects.filter(district=sdistrict,bloodgroup=bl)
	return render(request,'login.html',{"Doner":list(r)})



	
