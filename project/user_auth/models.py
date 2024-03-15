from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
# Create your models here.
class User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField( max_length=150, blank=True)
    last_name = models.CharField( max_length=150, blank=True)
    email = models.EmailField( blank=True)
    full_name = models.CharField(max_length=150, blank=True)

    objects=CustomUserManager()

    USERNAME_FIELD = "username"
