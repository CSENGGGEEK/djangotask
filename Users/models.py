from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    USER_TYPES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor')
    )
    utype = models.CharField(max_length=20, choices=USER_TYPES, default='patient')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return self.utype