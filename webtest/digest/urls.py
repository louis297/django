from django.conf.urls import url

from . import views

app_name = 'digest'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result$', views.result, name='result'),
    url(r'^empty$', views.empty, name='empty'),
]

##if settings.DEBUG and settings.STATIC_ROOT:
##    urlpatterns += static(settings.STATIC_URL,
##                          document_root=settings.STATIC_ROOT)
