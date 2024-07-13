from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView,DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import CustomUserCreationForm, UserProfileForm
from django.conf import settings
# Create your views here.

class UserRegisterView(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class UserProfileView(LoginRequiredMixin, DetailView):
    model = settings.AUTH_USER_MODEL
    template_name = 'accounts/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = settings.AUTH_USER_MODEL
    form_class = UserProfileForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserLogoutView(LogoutView):
    next_page = 'login'
