from django.db import models

# Create your models here.

class Donor(models.Model):
	
	name=models.TextField()
	bloodbank=models.TextField()
	district=models.TextField()
	number=models.BigIntegerField()
	email=models.TextField()
	password=models.TextField()
	bloodgroup=models.TextField()

	class Meta:
		db_table='doner'
    
	
