from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.conf.urls import patterns, include
from geonode.urls import urlpatterns as geonode_url_patterns
from maploom.geonode.urls import urlpatterns as maploom_urls

urlpatterns = patterns('',
                       (r'^file-service/', include('geoshape.file_service.urls')),
                       (r'^proxy/', 'geoshape.views.proxy'),
                       url(r'^robots.txt$',
                           TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),
                           name='robots'),
                       )

urlpatterns += geonode_url_patterns
urlpatterns += maploom_urls

import geonode
geonode.layers.admin.LayerAdmin.list_display =  (
        'id',
        'typename',
        'service_type',
        'title',
        'date',
        'category',
        'abstract',
        'data_quality_statement',
        'license',
        'regions',
        'keywords'
   )
