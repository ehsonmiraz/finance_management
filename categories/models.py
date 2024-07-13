from django.db import models
from django.db import models
from django.conf import settings
# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='categories')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
