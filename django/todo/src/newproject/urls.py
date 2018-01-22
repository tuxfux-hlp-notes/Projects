from django.conf.urls import include, url
from django.contrib import admin
from todo.views import status_report

urlpatterns = [
    # Examples:
    # url(r'^$', 'newproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^reports/', status_report,name="status_report"),
]
