from django.urls import path
from .views import (
    IndexView, NewCarouselImage, NewTomb, NewTombType
)

app_name  = 'dashboard'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('new/carousel/image', NewCarouselImage.as_view(), name='new_carousel_image'),
    path('new/tomb/type', NewTombType.as_view(), name='new_tomb_type'),
    path('new/tomb/<int:pk>', NewTomb.as_view(), name='new_tomb'),
]