from django import forms
from .models import SavingsGoal
from .validators import validate_future_date
class SavingsGoalForm(forms.ModelForm):
    target_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),validators=[validate_future_date])
    class Meta:
        model = SavingsGoal
        fields = ['name','target_amount', 'target_date']
