from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict

from crum import get_current_request

from LecturaPulsoSNW.settings import MEDIA_URL, STATIC_URL


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
