from django.db import models

# Create your models here.
class Users(models.Model):
	title = models.CharField(max_length=10)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	gender = models.PositiveSmallIntegerField()
	email = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	postcode = models.CharField(max_length=10)
	phone = models.CharField(max_length=15)
	dob = models.DateField()