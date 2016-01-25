from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Reviewer(AbstractBaseUser):
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField('email address', unique=True, db_index=True)
    country = CountryField()
    is_active = models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    USERNAME_FIELD='email'

    def __unicode__(self):
        return self.username
