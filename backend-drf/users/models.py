from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Abstractor = add/modify any fields in your present model.
# AbstractBaseUser = we use this if you want to get the full control over your user model.
# BaseUserManager = Employee.objects = Manager => he is the one who carries out all the actions on the model


class User(AbstractUser): # As we are going to modify email field as login field. By default User Name is the default login vaule.
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email