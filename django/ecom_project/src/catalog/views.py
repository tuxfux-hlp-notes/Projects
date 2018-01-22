from django.shortcuts import render,HttpResponse


# Create your views here.

def catalog(request):
	site_name = "Modern Musician"
	response_html = u"<html><body> Welcome to %s. </body></html>" % site_name
	return HttpResponse(response_html)


