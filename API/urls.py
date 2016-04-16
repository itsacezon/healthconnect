from django.conf.urls import url
from App.views import(
	ListBarangayAPIView,
	ListProgramAPIView,
	CreateProgramAPIView,
	CreateAttendeeAPIView,
	SendSMSAPIView,
)

urlpatterns = [
	url(r'^barangay', ListBarangayAPIView.as_view(), name='barangay-list'),
	url(r'^program/', CreateProgramAPIView.as_view(), name='program-create'),
	url(r'^program', ListProgramAPIView.as_view(), name='program-list'),
	url(r'^attendee/', CreateAttendeeAPIView.as_view(), name='attendee-create'),
	url(r'^send-sms', SendSMSAPIView.as_view(), name='send-sms'),
]


