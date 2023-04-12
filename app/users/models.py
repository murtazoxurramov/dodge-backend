import uuid
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (AbstractUser, UserManager)


class BaseModel(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    _validate_phone = RegexValidator(
        regex=r"^9\d{12}$",
        message="Telefon raqamingiz 9 bilan boshlanishi va 12 belgidan oshmasligi kerak! Masalan: 998900459442"
    )

    profile_image = models.FileField(
        upload_to='upload/user', blank=True, null=True
    )
    phone_number = models.CharField(
        max_length=12, unique=True, validators=[_validate_phone]
    )
    email = models.EmailField(blank=True, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
