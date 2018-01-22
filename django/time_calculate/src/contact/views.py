from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from contact.forms import ContactForm


def contact(request):
	errors = []
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'lead1429@mailinator.com'),
				['siteowner1429@mailinator.com'],
				)
			return HttpResponseRedirect('/contact/thanks')
		else:
			form = ContactForm()
		return render(request, 'contact_form.html', {'form': form})


	





























































