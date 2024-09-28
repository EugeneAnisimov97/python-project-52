from django.db import models
from django.core.exceptions import ValidationError
import re


# Create your models here.
def validate_username(user_name):
    if not re.match(r'^[0-9A-Za-z@.+/-_]+$', user_name):
        raise ValidationError(
            'Только буквы, цифры и символы @/./+/-/_.')


class users(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
