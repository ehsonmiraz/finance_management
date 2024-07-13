from django import forms
from .models import Transaction
from categories.models import Category

class TransactionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'category', 'description','type']

    def __init__(self,user,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['category'].queryset = user.categories.all()