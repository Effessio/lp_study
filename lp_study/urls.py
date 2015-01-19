from django.conf.urls import patterns, include, url
from django.contrib import admin
from mds.views import ItemList, increase_count, LowQuantity

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lp_study.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ItemList.as_view()),
    url(r'increase_count/(?P<pk>\d+)$', increase_count, name='increase_count'),
    url(r'low_quantity$', LowQuantity.as_view(), name='low_quantity'),

)
