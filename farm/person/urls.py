from django.views import generic
from django.conf.urls import url
from .models import Person

urlpatterns = [
    url(r'^$', generic.ListView.as_view(model=Person), name='index'),
]