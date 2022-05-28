from django import forms
from django.forms import ModelForm

from .models import MortgageInfo


class MortgageInfoForm(ModelForm):
    class Meta:
        model = MortgageInfo
        fields = '__all__'
