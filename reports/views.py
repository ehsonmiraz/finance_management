from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import Transaction
from datetime import datetime
from django.db.models import Sum
from .forms import ReportForm

class ReportView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        form = ReportForm()
        context = {'form': form}
        return render(request, 'reports/report_form.html', context)

    def post(self, request, *args, **kwargs):
        form = ReportForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            print(type(month),year)
            # Calculate Yearly totals for expenses and debit transactions
            if month == '0':
               expenses = self.request.user.transactions.filter(date__year=year,type='Debit')
               income = self.request.user.transactions.filter(date__year=year,type='Credit').aggregate(Sum('amount'))['amount__sum'] or 0
    
            # Calculate monthly totals for expenses and debit transactions   
            else:
               expenses = self.request.user.transactions.filter(date__year=year, date__month=month, type='Debit')
               income = self.request.user.transactions.filter(date__year=year, date__month=month, type='Credit').aggregate(Sum('amount'))['amount__sum'] or 0


            # Calculate category-wise debit expenses for the pie chart
            category_expenses = {}
            for transaction in expenses:
                category_name = transaction.category.name
                if category_name in category_expenses:
                    category_expenses[category_name] += transaction.amount
                else:
                    category_expenses[category_name] = transaction.amount
       
            labels=[]
            data=[]
            for label,amount in category_expenses.items():
                labels.append(str(label))
                data.append(int(amount))
            print(type(data))
            total_expenditure=sum(data)
            context = {
                'month': month,
                'year': year,
                'total_expenditure': total_expenditure,
                'income': income,
                'labels': labels,
                'data': data,
            }
            return render(request, 'reports/report.html', context)

        context = {'form': form}
        return render(request, 'reports/report_form.html', context)
