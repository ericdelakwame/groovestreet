from email.policy import default
from tabnanny import verbose
from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from django.contrib.gis.db.models import PointField
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

User = get_user_model()


class CarouselImage(models.Model):
    image = models.ImageField(upload_to='ome/carousel/images/%Y/%m/%d', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Carousel Image'
        verbose_name_plural = 'Carousel Images'
    
    def __str__(self):
        return 'Carousel Image: {}'.format(str(self.created))

class TombType(models.Model):
    summary = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'Tomb Type'
        verbose_name_plural = 'Tomb Types'

    def __str__(self):
        return self.summary

    def get_absolute_url(self):
        return reverse('home:tomb_type_detail', kwargs={'pk': self.pk})

class Tomb(models.Model):
    tomb_type = models.ForeignKey(TombType, related_name='tombs', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    description = RichTextField()
    location = PointField()
    tags = TaggableManager()
    curator = models.ForeignKey(User, related_name='tombs', on_delete=models.CASCADE, null=True) 
    created = models.DateTimeField(auto_now_add=True)


    class Meta: 
        verbose_name = 'Tomb'
        verbose_name_plural = 'Tombs'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:tomb_detail', kwargs={'pk': self.pk})


