from django.db import models

# Create your models here.

import datetime

class List(models.Model):
	title = models.CharField(max_length=250,unique=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering=['title']


PRIORITY_CHOICES = (
	(1,'Low'),
	(2,'Normal'),
	(3,'High'),
	)

class Item(models.Model):
	title = models.CharField(max_length=250)
	create_date = models.DateTimeField(default=datetime.datetime.now)
	priority = models.IntegerField(choices=PRIORITY_CHOICES,default=2)
	completed = models.BooleanField(default=False)
	todo_list = models.ForeignKey(List)

	def __unicode__(self):
		return self.title
	class Meta:
		ordering = [ '-priority','title']