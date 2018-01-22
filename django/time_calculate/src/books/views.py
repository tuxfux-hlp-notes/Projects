from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.

"""first create front-end search view and create associated 
template(search_form.html) in second step create 'query' 
handler view and create asscoicted query hanlder template
(search_results.html) and hook these 2 views in urls

# frontend search form

def search_form(request):
	return render(request, 'search_form.html')

#backend 'query' handler 

def search(request):
	#aside from checking that 'q' exists in request.GET 
	#we also make sure that request.GET['q'] is non-empty value
	if 'q' in request.GET and request.GET['q']: 
		q= request.GET['q'] #instance 
		#icontains is a lookup type
		books = Book.objects.filter(title__icontains=q)
		return render(request, 'search_results.html',
			{'books':books, 'query':q})
	else:
		return render(request, 'search_form.html', 
			{'error': True})
"""

#UPDATED VERSION OF SEARCH NO NEED OF 2 VIEW FUNCTIONS

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.') 
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html', 
				{'books': books, 'query': q})
	return render(request, 'search_form.html', 
		{'errors': errors})








































































