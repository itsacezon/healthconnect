from __future__ import unicode_literals

from django.db import models

from django.contrib.postgres.fields import ArrayField, JSONField
# Create your models here.

class User(models.Model):
	full_name = models.CharField(max_length = 50, blank = False, db_index = True)
	address =  models.CharField(max_length = 50, blank = False, db_index = True)
	barangay_id  = models.IntegerField(blank = False, db_index = True)
	phone_number = models.CharField(max_length = 15, blank = False, db_index = True)

class Barangay(models.Model):
	full_name = models.CharField(max_length = 50, blank = False, db_index = True)
	city = models.CharField(max_length = 50, blank = False, db_index = True)
	region = models.CharField(max_length = 50, blank = False, db_index = True)
	province = models.CharField(max_length = 50, blank = False, db_index = True)

class HealthProgram(models.Model):
	title = models.CharField(max_length = 50, blank = False, db_index = True)
	barangay_id  = models.IntegerField(blank = False, db_index = True)
	created_at = models.DateTimeField(auto_now_add = True)
	tags = ArrayField(models.CharField(max_length = 20), default = [])
	sessions = JSONField(default=[])

class Attendance(models.Model):
	session_id = models.IntegerField(blank = False)
	user_id = models.IntegerField(blank = False)
	remark = models.TextField(blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	

