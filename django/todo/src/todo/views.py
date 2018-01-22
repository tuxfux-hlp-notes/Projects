from django.shortcuts import render
from .models import List

# Create your views here.

def status_report(request):
	todo_listing = []
	for todo_list in List.objects.all():
		todo_dict = {}
		todo_dict['list_object'] = todo_list
		todo_dict['item_count'] = todo_list.item_set.count()
		todo_dict['items_completed'] = todo_list.item_set.filter(completed=True).count()
		#print float(todo_dict['items_completed']),todo_dict['item_count']
		if todo_dict['item_count'] == 0:
			todo_dict['percent_completed'] = 'No Items with same name'
		else:
			todo_dict['percent_completed'] = int(float(todo_dict['items_completed']) / todo_dict['item_count'] * 100)
		todo_listing.append(todo_dict)
	return render(request, 'status_report.html',{'todo_listing':todo_listing})
