from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, TemplateView, FormView, DetailView
)
from django.urls import reverse_lazy
from django.views.generic.edit import (
    FormMixin, UpdateView, DeleteView, CreateView
)

from home.models import (
    CarouselImage, TombType, Tomb
)
from home.forms import CarouselImageForm, TombForm, TombTypeForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    template_name = 'dashboard/index.html'

class NewCarouselImage(FormView):
    template_name = 'dashboard/forms/carousel_image_form.html'
    form_class = CarouselImageForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        image = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



class NewTombType( LoginRequiredMixin, FormView):
    login_url = '/accounts/login'
    template_name = 'dashboard/forms/tomb_type_form.html'
    form_class = TombTypeForm
    success_url = reverse_lazy('dashboard:index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class NewTomb(LoginRequiredMixin, FormView):
    login_url = '/accounts/login'
    template_name = 'dashboard/forms/tom_form.html'
    form_class = TombForm

    def form_valid(self, form):
        tomb_type = TombType.objects.get(pk=self.kwargs['pk'])
        tomb = form.save(commit=False)
        tomb.tomb_type = tomb_type
        tomb.curator = self.request.user
        tomb.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
