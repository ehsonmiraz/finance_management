from django.urls import path
from .views import SavingsGoalListView, SavingsGoalCreateView, SavingsGoalUpdateView, SavingsGoalDeleteView

urlpatterns = [
    path('', SavingsGoalListView.as_view(), name='savingsgoal_list'),
    path('create/', SavingsGoalCreateView.as_view(), name='savingsgoal_create'),
    path('<int:pk>/update/', SavingsGoalUpdateView.as_view(), name='savingsgoal_update'),
    path('<int:pk>/delete/', SavingsGoalDeleteView.as_view(), name='savingsgoal_delete'),
]
