import uuid
import random
from datetime import datetime, timedelta
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (AbstractUser, UserManager)


VIA_PHONE, VIA_EMAIL, VIA_USERNAME = (
    "via_phone",
    "via_email",
    "via_username"
)


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
    AUTH_TYPE_CHOICES = (
        (VIA_PHONE, VIA_PHONE),
        (VIA_EMAIL, VIA_EMAIL),
        (VIA_USERNAME, VIA_USERNAME)
    )

    profile_image = models.FileField(
        upload_to='upload/user', blank=True, null=True
    )
    auth_type = models.CharField(
        max_length=31, choices=AUTH_TYPE_CHOICES, default=VIA_USERNAME
    )
    phone_number = models.CharField(
        max_length=12, unique=True, validators=[_validate_phone]
    )
    email = models.EmailField(blank=True, null=True)
    last_login_code = models.CharField(max_length=6, blank=True, null=True)
    last_login_code_time = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def check_username(self):
        if not self.username:
            temp_username = f"DemoProject-{uuid.uuid4().__str__().split('-')[-1]}"
            while User.objects.filter(username=temp_username):
                temp_username = f"{temp_username}{random.randint(0,9)}"

            self.username = temp_username

    def check_email(self):
        if self.email:
            normilized_email = self.email.lower()
            self.email = normilized_email

    def check_pass(self):
        if not self.password:
            temp_password = f"password{uuid.uuid4().__str__().split('-')[-1]}"
            self.password = temp_password

    def hashing_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.clean()

        super(User, self).save(*args, **kwargs)

    def clean(self):
        self.check_email()
        self.check_username()
        self.check_pass()
        self.hashing_password()
