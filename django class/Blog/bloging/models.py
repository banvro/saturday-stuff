from django.db import models

# Create your models here.

class contactUs(models.Model):
    name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    phon_nmbr = models.IntegerField()
    message = models.TextField()


