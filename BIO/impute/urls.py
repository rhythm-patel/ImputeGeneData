from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('nmc', views.nmc, name='nmc'),
	path('dapl', views.dapl, name='dapl')
	# path('input_list', views.input_list, name='input_list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)