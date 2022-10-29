from django import forms
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.gis.forms.fields import PointField
from mapwidgets.widgets import GooglePointFieldWidget


class NewUserForm(UserCreationForm):    
    location = PointField(widget=GooglePointFieldWidget())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']