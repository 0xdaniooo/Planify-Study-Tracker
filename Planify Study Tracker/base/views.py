from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.contrib.auth.models import User

from .forms import SignUpForm, EditAccountForm, PasswordDataChangeForm

# Main functionality page
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'base/home.html'
    def get_login_url(self):
        return '/get_started/'

# Landing page
def GetStartedPage(request):
    return render(request, 'base/get_started.html')

# Allows for account creation
class SignUpPage(FormView):
    template_name = 'base/signup.html'
    form_class = SignUpForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(SignUpPage, self).get(*args, **kwargs)

# Login to existing account
class LoginPage(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')

# Allows for modification of username and email
class EditAccountPage(LoginRequiredMixin, UpdateView):
    template_name = 'base/edit_account.html'
    form_class = EditAccountForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

# Allows for a password change
class ChangePasswordPage(LoginRequiredMixin, PasswordChangeView):
    template_name = 'base/change_password.html'
    form_class = PasswordDataChangeForm
    success_url = reverse_lazy('home')

def password_success(request):
    return render(request, 'base/account_management.html', {})

# Allows the user to delete their account
class DeleteAccountPage(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'base/delete_account.html'
    success_url = reverse_lazy('get-started')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        logout(request)
        return super().delete(request, *args, **kwargs)
