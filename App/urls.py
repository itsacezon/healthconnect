from django.conf.urls import url, include, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
	DoctorList
)

urlpatterns = [
	url(r'^api/', DoctorList.as_view(), name='doctor-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
