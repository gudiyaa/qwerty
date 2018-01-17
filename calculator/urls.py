from django.conf.urls import url, include
from .views import Base

urlpatterns=[
	url(r'^$', Base.as_view(), name='base'),
]