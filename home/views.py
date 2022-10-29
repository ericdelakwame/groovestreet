from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    TemplateView, ListView, DetailView
)
from .models import CarouselImage



class IndexView(TemplateView):
    template_name = 'home/index.html'

    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        carousel_images = CarouselImage.objects.order_by('-created')
        context['carousel_images'] = carousel_images
        return context
    

