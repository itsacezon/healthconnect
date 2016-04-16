from rest_framework import serializers
from .models import User, Barangay, HealthProgram, Attendance


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User

class BarangaySerializer(serializers.ModelSerializer):
	class Meta:
		model = Barangay


class HealthProgramSerializer(serializers.ModelSerializer):
	class Meta:
		model = HealthProgram

	def to_representation(self, instance):
		data = super(HealthProgramSerializer, self).to_representation(instance)
		data["barangay_name"] = Barangay.objects.get(pk = data["barangay_id"]).full_name
	
		return data

class AttendanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Attendance