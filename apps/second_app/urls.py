from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^travels$', views.travels),
    url(r'^add$', views.add),
    url(r'^addtrip$', views.addtrip),
    url(r'^destination$', views.destination),
    url(r'^trip/(?P<id>\d+)$', views.trip),

]
