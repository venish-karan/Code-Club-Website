from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	title = models.CharField(max_length=100, null=True)
	description = models.TextField()
	poster = models.ImageField(upload_to='posters', null=True, blank=False)
	date_posted = models.DateField(auto_now_add=True, null=True)
	end_date = models.DateField(null=True)
	form_link = models.CharField(max_length=200)

	def __str__(self):
		return str(self.title)

class Gallery(models.Model):
	title = models.CharField(max_length=300)
	image = models.ImageField(upload_to='gallery', null=False, blank=False)

	def __str__(self):
		return str(self.title)

		