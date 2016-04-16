from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import User, Barangay, HealthProgram, Attendance

from .serializers import (
	UserSerializer, 
	BarangaySerializer, 
	HealthProgramSerializer,
	AttendanceSerializer
)

# Create your views here.


def home(request):
    context = {}
    return render(request, "index.html", context)

class ListBarangayAPIView(APIView):
	
	serializer_class = BarangaySerializer

	def get_permission(self):
		return[AllowAny()]

	def get(self, request):
		queryset = Barangay.objects.all()
		serializer = self.serializer_class(queryset, many = True)
		return Response(serializer.data)

class ListProgramAPIView(APIView):
	
	serializer_class = HealthProgramSerializer

	def get_permission(self):
		return[AllowAny()]

	def get(self, request):
		queryset = HealthProgram.objects.all()
		serializer = self.serializer_class(queryset, many = True)
		return Response(serializer.data)

class CreateProgramAPIView(APIView):

	serializer_class = HealthProgramSerializer

	def post(self, request, format=None):
		data = request.data
		serializer = HealthProgramSerializer(data=data)
		if serializer.is_valid():
			
			report = serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# class DoctorList(generics.ListCreateAPIView):
# 	"""
# 	API endpoint for listing and creating Book objects
# 	"""
# 	queryset = Doctor.objects.all()
# 	serializer_class = DoctorSerializer
#     