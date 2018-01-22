from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.

def archieve(request):
  posts = BlogPost.objects.all()
  context = {'posts':posts}
  return render(request,'archieve.html',context)


