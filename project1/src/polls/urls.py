from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]



# references
# https://docs.djangoproject.com/en/1.11/intro/tutorial01/#url-argument-regex