from django.conf.urls import url

from . import views

# https://docs.djangoproject.com/en/1.11/intro/tutorial03/#namespacing-url-names
app_name='polls'
urlpatterns = [
 	# ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]



# references
# https://docs.djangoproject.com/en/1.11/intro/tutorial01/#url-argument-regex