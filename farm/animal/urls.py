from django.views import generic
from django.conf.urls import url
from .models import Animal

urlpatterns = [
    url(r'^$', generic.ListView.as_view(model=Animal), name='index'),
]