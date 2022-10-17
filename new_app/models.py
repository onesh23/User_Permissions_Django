from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



# Create your models here.


class User(AbstractUser):
    is_superuser= models.BooleanField('Is superuser', default=False)
    is_admin = models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=False)




alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class VehicleModel(models.Model):
    CHOICES = (
        ('TWO_WHEELER', '2'),
        ('THREE_WHEELER', '3'),
        ('FOUR_WHEELER', '4')
    )

    vehicle_number = models.CharField(max_length=50, blank=False, null=False, validators=[alphanumeric])
    Vehicle_type = models.CharField(max_length=50,choices=CHOICES)

    vehicle_model = models.CharField(max_length=23)
    vehicle_description = models.TextField()

    def __str__(self):
        return self.vehicle_number
