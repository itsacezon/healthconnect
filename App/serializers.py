from rest_framework import serializers
from .models import User, Barangay, HealthProgram, Attendance


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User

class BarangaySerializer(serializers.ModelSerializer):
	class Meta:
		model = Barangay

class CreateHealthProgramSerializer(serializers.ModelSerializer):
	class Meta:
		model = HealthProgram

class HealthProgramSerializer(serializers.ModelSerializer):
	class Meta:
		model = HealthProgram
		sessions = serializers.ListField(
			child=serializers.DictField()
		)
	def to_representation(self, instance):
		data = super(HealthProgramSerializer, self).to_representation(instance)
		data["barangay_name"] = Barangay.objects.get(pk = data["barangay_id"]).full_name

		import ast, json
		sessions = ast.literal_eval(data['sessions'])
		for item in sessions:
			item['attendees'] = []
			attendees = Attendance.objects.filter(health_program_id=data['id'], session_id=item['id'])
			for x in attendees:
				item['attendees'].append(x.user_id)
		data['sessions'] = sessions
		return data

class AttendanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Attendance