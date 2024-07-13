from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SavingsGoal
from .forms import SavingsGoalForm
from django.db.models import Sum
from datetime import datetime
from calendar import monthrange
# Create your views here.
class SavingsGoalListView(LoginRequiredMixin, ListView):
    model = SavingsGoal
    template_name = 'goals/savingsgoal_list.html'
    def get_context_data(self,**kwargs):
            context = super().get_context_data(**kwargs)
            live_goals = SavingsGoal.objects.filter(user=self.request.user, status='live')
            net_income_of_current_month=self.request.user.transactions.filter(date__month=datetime.now().month,type='Credit').aggregate(sum=Sum('amount'))['sum'] or 0
            net_expense_of_current_month=self.request.user.transactions.filter(date__month=datetime.now().month,type='Debit').aggregate(sum=Sum('amount'))['sum'] or 0
            budget_per_day=net_income_of_current_month/monthrange(datetime.now().year,datetime.now().month)[1]
            expense_per_day=net_expense_of_current_month/datetime.now().day
            savings_per_day=int(budget_per_day)-int(expense_per_day)
            if(savings_per_day<0):
                 savings_per_day=0
            savings=savings_per_day*datetime.now().day  

            # Update status of past due goals
            for goal in live_goals:
                if goal.is_past_due() and goal.status == 'live':
                    if(savings>goal.target_amount):
                         goal.status = 'completed'
                    else:      
                        goal.status = 'failed'
                    goal.save()
            context['savings']=savings
            context['live_goals'] = live_goals
            context['past_goals'] = SavingsGoal.objects.filter(user=self.request.user).exclude(status='live')
            return context        
        
            
class SavingsGoalCreateView(LoginRequiredMixin, CreateView):
    model = SavingsGoal
    form_class = SavingsGoalForm
    template_name = 'goals/savingsgoal_form.html'
    success_url = reverse_lazy('savingsgoal_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SavingsGoalUpdateView(LoginRequiredMixin, UpdateView):
    model = SavingsGoal
    form_class = SavingsGoalForm
    template_name = 'goals/savingsgoal_form.html'
    success_url = reverse_lazy('savingsgoal_list')

class SavingsGoalDeleteView(LoginRequiredMixin, DeleteView):
    model = SavingsGoal
    template_name = 'goals/savingsgoal_confirm_delete.html'
    success_url = reverse_lazy('savingsgoal_list')
