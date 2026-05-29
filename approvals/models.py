from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Company

User = get_user_model()


class ApprovalWorkflow(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)

    module = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ApprovalStep(models.Model):
    workflow = models.ForeignKey(
        ApprovalWorkflow,
        on_delete=models.CASCADE,
        related_name='steps'
    )

    step_number = models.IntegerField()

    approver = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"{self.workflow.name} - Step {self.step_number}"


class ApprovalRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    workflow = models.ForeignKey(
        ApprovalWorkflow,
        on_delete=models.CASCADE
    )

    reference_id = models.BigIntegerField()

    module = models.CharField(max_length=100)

    requested_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    current_step = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.module} Approval"