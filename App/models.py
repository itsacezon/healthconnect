from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Doctor(models.Model):
	full_name = models.CharField(max_length = 50, blank = False)

	def __unicode__(self):
		return self.full_name