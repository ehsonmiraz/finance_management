from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_date(value):
    today = timezone.now().date()
    if value < today:
        raise ValidationError('Select a date in the future.')