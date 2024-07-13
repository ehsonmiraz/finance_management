from django.db import models
from django.db import models
from django.conf import settings
from categories.models import Category

# Create your models here.
class Transaction(models.Model):
    TYPE_CHOICES = [
        ('Debit', 'Debit'),
        ('Credit', 'Credit'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    
    type = models.CharField(max_length=10, choices=TYPE_CHOICES,default='debit')
    def __str__(self):
        return f"{self.category}: {self.amount}"
