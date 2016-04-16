from django.shortcuts import render
from django.http import HttpResponseRedirect
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

import uuid

# Create your views here.

CHIKKA_SMS_API_POST_URL = 'https://post.chikka.com/smsapi/request'
SHORTCODE = '29290134'

def home(request):
    context = {}
    return render(request, "index.html", context)

def generate_msgid():
    """Generate random and unique alphanumeric ID"""
    return uuid.uuid4().hex

def send_sms(mobile_number, message):
    import requests as http
    msg_id = generate_msgid()
    payload = { 'message_type'  : 'SEND',
                'mobile_number' : mobile_number, 
                'shortcode'     : SHORTCODE,
                'message_id'    : msg_id,
                'message'       : message,
                'client_id'     : '9e282fc73f0de1a3bb24082150953269dc94990f68fb9b9cfab2b20c19500b40',
                'secret_key'    : '078069255f2fa862dd948e13eb47dcef612badff3a83caf759e580ab7854b703'
              }
    resp = http.post(CHIKKA_SMS_API_POST_URL, data=payload)
    try:
        info = dict(resp.json())
        print(info)
        status = info.get("status")
        stsmsg = info.get("message")
        if status == "200":
            #message was accepted by API for sending
            pass  #TODO: Code when sending to API is ok
        elif status == "400":
            #when something is wrong with request
            desc  = info.get("description") 
            raise SMSSendError(stsmsg, desc)
        elif status in ("401", "403", "404"):
            #401 means your credentials (client_id, sec. key) are incorrect
            #403 means you did not use POST
            #404 means CHIKKA_SMS_API_POST_URL is incorrect
            raise SMSSendError(stsmsg, None)
        elif status == "500":
            #Something is not right with the SMS API Server
            raise SMSSendError(stsmsg, None)
    except ValueError:
        raise SMSSendError('Response is not JSON', resp)

class SendSMSAPIView(APIView):
     def get(self, request):
        
        send_sms('639176302364', 'I love you <3')
        return Response({}, status.HTTP_200_OK)


class ListBarangayAPIView(APIView):
    
    serializer_class = BarangaySerializer

    def get_permission(self):
        return[AllowAny()]

    def get(self, request):
        queryset = Barangay.objects.all()
        serializer = self.serializer_class(queryset, many = True)
        return Response(serializer.data)

class ListProgramAPIView(APIView):
    
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer

    def get_permission(self):
        return[AllowAny()]

    def filter_queryset(self, queryset):
        filters = {}
        if self.request.GET.get('barangay', None):

            filters['barangay_id'] = self.request.GET.get('barangay', None)

        queryset = queryset.filter(**filters)
        return queryset

    def get(self, request):
        queryset = self.queryset
        queryset = self.filter_queryset(queryset)
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

class CreateAttendeeAPIView(APIView):

    serializer_class = AttendanceSerializer

    def post(self, request, format=None):
        data = request.data
        serializer = AttendanceSerializer(data=data)
        if serializer.is_valid():
            
            report = serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# class DoctorList(generics.ListCreateAPIView):
#   """
#   API endpoint for listing and creating Book objects
#   """
#   queryset = Doctor.objects.all()
#   serializer_class = DoctorSerializer
#     