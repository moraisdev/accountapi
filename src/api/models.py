from django.db import models

class Account(models.Model):
    fullName = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    document = models.CharField(max_length=12, unique=True)
    birthDate = models.DateField()

    class Meta:
        verbose_name='Account'
        verbose_name_plural='Accounts'