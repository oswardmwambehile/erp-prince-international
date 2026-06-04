from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    tin_number = models.CharField(max_length=100)
    vrn_number = models.CharField(max_length=100)

    currency = models.CharField(max_length=20, default='TZS')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name