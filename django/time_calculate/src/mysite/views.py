from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime





def hello(request):
	return HttpResponse("Hello world")

def my_homepage_view(request):
	return HttpResponse("Welcome to 'Django' buddy ")

def current_datetime(request):
	now = datetime.datetime.now()
	#t = get_template('current_datetime.html')
	return render(request, 'current_datetime.html', {'current_date': now})
	#html = t.render(Context({'current_date': now}))
	#return HttpResponse(html)


def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s. </body></html>" % (offset, dt)
	return HttpResponse(html)

def book_list(request):
	db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
	
def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' %(k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))






















