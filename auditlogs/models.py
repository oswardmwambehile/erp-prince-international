from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Company

User = get_user_model()


class AuditLog(models.Model):
    ACTION_CHOICES = (
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('approve', 'Approve'),
        ('reject', 'Reject'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    module = models.CharField(max_length=100)

    record_id = models.CharField(max_length=255)

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action}"