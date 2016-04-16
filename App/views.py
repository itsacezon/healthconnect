from django.shortcuts import render
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
# Create your views here.


def home(request):
    context = {}
    return render(request, "index.html", context)

class DoctorList(generics.ListCreateAPIView):
	"""
	API endpoint for listing and creating Book objects
	"""
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer
    