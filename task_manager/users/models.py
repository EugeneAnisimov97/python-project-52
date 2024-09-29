from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
import re


# Create your models here.
def validate_username(user_name):
    if not re.match(r'^[0-9A-Za-z@.+/-_]+$', user_name):
        raise ValidationError(
            'Только буквы, цифры и символы @/./+/-/_.')


class Users(models.Model):
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, unique=True, validators=[validate_username])
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        return check_password(password, self.password)
