from __future__ import unicode_literals

from django.db import models


# Create your models here.

def User(models.Model): 
	first = models.Charfield(max_length=15)
	last = models.Charfield(max_length=25)
	middle = models.Charfield(max_length=1)
	hometown = models.Charfield(max_length=20) # will use a Destination object later
	country = models.Charfield(max_length=20) # will change to django_countries module later
	#contact will be it's own model of phone, email, facebook  
	


"""
def Destinations(models.Model): 
	pass


def Contacts(models.Model): 
	pass 


def Blogs(models.Model): 
	pass


def Videos(models.Model):
	pass

#find way to save routes
def Routes(models.Model):
	pass
"""

