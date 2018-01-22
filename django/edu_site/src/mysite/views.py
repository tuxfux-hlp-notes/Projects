from django.shortcuts import render

# Create your views here.

def myhome(request):
    context={}
    return render(request,'home.html',context)

def contactus(request):
	context={}
	return render(request,'contact-us.html',context)

def aboutus(request):
	context={}
	return render(request,'about-us.html',context)
