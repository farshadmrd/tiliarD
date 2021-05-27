import uuid
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class User(AbstractUser, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    created_at = models.DateTimeField(default=now())
    modified_at = models.DateTimeField(default=now())
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[RegexValidator("^[+]?[0-9]*$")],
    )
