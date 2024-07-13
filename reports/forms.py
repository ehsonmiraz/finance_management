# reports/forms.py

from django import forms
from datetime import datetime
class ReportForm(forms.Form):
    MONTH_CHOICES = [
        (0,'No selection'),
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
        
    ]
    YEAR_CHOICES = [(year, year) for year in range( datetime.now().year, 2000,-1)]

    month = forms.ChoiceField(choices=MONTH_CHOICES, label='Month')
    year = forms.ChoiceField(choices=YEAR_CHOICES, label='Year')
