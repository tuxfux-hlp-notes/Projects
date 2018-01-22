from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'edu_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','mysite.views.myhome', name='home'),
    url(r'^contact/','mysite.views.contactus',name='contact'),
    url(r'^aboutus/','mysite.views.aboutus',name='aboutus'),
]
