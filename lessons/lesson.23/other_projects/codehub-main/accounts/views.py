from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from snippets.models import Snippet
from tickets.models import Comment, Ticket

from .forms import (CustomPasswordChangeForm, CustomUserCreationForm,
                    CustomUserUpdateForm)
from .models import User


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        if request.user.is_authenticated:
            raise PermissionDenied()
        else:
            return super().get(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = "profile.html"
    success_url = reverse_lazy('profile')

    def get_object(self, *args, **kwargs):
        user = User.objects.get(username=self.request.user)
        return user

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)

        context['snippets'] = Snippet.objects.filter(
            created_by=self.request.user.id
        ).order_by('-created_on')

        context['tickets'] = Ticket.objects.filter(
            created_by=self.request.user.id
        ).order_by('-created_on')

        context['comments'] = Comment.objects.filter(
            created_by=self.request.user.id
        ).order_by('-created_on')

        return context


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('home')
    form_class = CustomPasswordChangeForm


class CustomLoginView(LoginView):
    def get(self, request: HttpRequest, *args: str, **kwargs):
        if request.user.is_authenticated:
            raise PermissionDenied()
        else:
            return super().get(request, *args, **kwargs)
