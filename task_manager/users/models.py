from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    AbstractUser
)


# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.get_full_name()