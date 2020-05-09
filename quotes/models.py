from django.db import models
from itertools import chain
#from .views import output

class stonk(models.Model):
	ticker=models.CharField(max_length=10)

	def __str__(self):
		return self.ticker







