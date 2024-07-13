from django.db import models
from django.conf import settings
from django.utils import timezone
from .validators import validate_future_date
class SavingsGoal(models.Model):
    STATUS_CHOICES = (
        ('live', 'Live'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)

    target_date = models.DateField(validators=[validate_future_date])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='live')

    def __str__(self):
        return self.name

    def is_past_due(self):
        return self.target_date < timezone.now().date()
