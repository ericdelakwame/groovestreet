from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, DetailView, FormView, TemplateView
)
from django.views.generic.edit import (
    UpdateView, DeleteView
)
from .forms import NewUserForm


class RegisterView(FormView):
    template_name = 'accounts/forms/signup_form.html'
    form_class = NewUserForm
    success_url = '/accounts/profile'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


@login_required(login_url='/accountslogin')
def profile(request):
    if request.user.is_superuser:
        return redirect('dashboard:index')
    else:
        return redirect('home:index')

