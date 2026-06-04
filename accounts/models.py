from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


# =========================
# COMPANY MODEL
# =========================
class Company(models.Model):
    name = models.CharField(max_length=255)

    code = models.CharField(
        max_length=50,
        unique=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# =========================
# BRANCH MODEL
# =========================
class Branch(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='branches'
    )

    name = models.CharField(max_length=255)

    code = models.CharField(
        max_length=50,
        unique=True
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# =========================
# DEPARTMENT MODEL
# =========================
class Department(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=255)

    code = models.CharField(
        max_length=50,
        unique=True
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# =========================
# ROLE / POSITION MODEL
# =========================
class Position(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=255)

    description = models.TextField(
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# =========================
# CUSTOM USER MANAGER
# =========================
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Email must be provided")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)

        return self.create_user(
            email,
            password,
            **extra_fields
        )


# =========================
# CUSTOM USER MODEL
# =========================
class User(AbstractBaseUser, PermissionsMixin):

    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    email = models.EmailField(unique=True)

    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    contact = models.CharField(
        max_length=13,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^(?:\+255|0)[67][0-9]{8}$',
                message='Enter valid Tanzanian number'
            )
        ]
    )

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(
        default=timezone.now
    )
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def get_short_name(self):
        return self.first_name