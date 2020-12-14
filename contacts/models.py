from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='contacts', blank=True, default='', on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=True, default='')
    telephone = models.CharField(max_length=16, blank=True, default='')
    email = models.CharField(max_length=80, blank=True, default='')
    created_date = models.DateField(auto_now_add=True)


class Address(models.Model):
    street = models.CharField(max_length=100, blank=True, default='')
    extra_info = models.CharField(max_length=100, blank=True, default='')
    zip_code = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    number = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="addresses"
    )
