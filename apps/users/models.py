from django.core.exceptions import ValidationError
import re
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager, Permission
from django.utils.translation import gettext_lazy as _
from apps.common import models as common


def validate_phone(value):
    phone_regex = re.compile(r'^\+998\d{9}$')
    if not phone_regex.match(value):
        raise ValidationError({"phone": "Phone is not valid"})


class UserManager(AbstractUserManager):
    def _create_user(self, phone, password, **extra_fields):
        """
        Create and save a user with the given phone and password.
        """
        if not phone:
            raise ValueError("The given phone number must be set")

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone, password, **extra_fields)

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser, common.BaseModel):
    REQUIRED_FIELDS = []
    email = None
    username = None

    phone = models.CharField(max_length=255, validators=[validate_phone], unique=True)
    objects = UserManager()
    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"{self.phone} || {self.first_name}"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def check_and_set_password(self):
        if self.password and not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

    def save(self, *args, **kwargs):
        self.check_and_set_password()  # Rename method to avoid conflict
        super(User, self).save(*args, **kwargs)


def __str__(self):
    return f"{self.name}"


Permission.__str__ = __str__
