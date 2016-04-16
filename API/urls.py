from django.conf.urls import url
from App.views import(
	ListBarangayAPIView,
	ListProgramAPIView,
	CreateProgramAPIView,
)

urlpatterns = [
	url(r'^barangay', ListBarangayAPIView.as_view(), name='barangay-list'),
	url(r'^program/', CreateProgramAPIView.as_view(), name='program-create'),
	url(r'^program', ListProgramAPIView.as_view(), name='program-list'),
]


