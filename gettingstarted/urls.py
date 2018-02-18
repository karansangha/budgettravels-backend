from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin

admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^list_attractions/(?P<city_id>\w{1,50})/$', hello.views.list_attractions, name='list_attractions'),
    url(r'^attraction/(?P<attraction_id>\w{1,50})/$', hello.views.attraction, name='attraction'),
    url(r'^attraction/(?P<attraction_id>\w{1,50})', hello.views.attraction, name='attraction'),
    path('admin/', admin.site.urls),
]
