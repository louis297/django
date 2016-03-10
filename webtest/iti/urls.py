from django.conf.urls import url

from . import views

app_name = 'iti'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^send$', views.send, name='send'),
    url(r'^success$', views.success, name='success'),
    url(r'^history$', views.history, name='history'),
    url(r'^fail$', views.fail, name='fail'),
    url(r'^history/(?P<pk>[0-9]+)', views.transaction, name='transaction'),
    url(r'^del/(?P<pk>[0-9]+)', views.del_trans, name='delete transaction'),
]
