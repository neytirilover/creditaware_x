from django.conf.urls import *
from views import test_page

urlpatterns = [
    url(r'^$', test_page, name = 'Credit Card Info Management'),
]
