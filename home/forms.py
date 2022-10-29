from django import forms
from django import forms
from .models import CarouselImage, TombType, Tomb
from ckeditor.fields import RichTextFormField


class CarouselImageForm(forms.ModelForm):

    class Meta:
        model = CarouselImage
        fields = ['image']



class TombTypeForm(forms.ModelForm):

    class Meta:
        model = TombType
        fields = ['summary']



class TombForm(forms.ModelForm):
    description = RichTextFormField()

    class Meta:
        model = Tomb
        exclude = ['curator', 'created']