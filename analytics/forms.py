from django import forms
from django.forms.forms import Form

class AnalyticsFilterForm(Form):
    """ Helps to filter Events for a daterange """
    date_from = forms.DateField(required=False)
    date_to = forms.DateField(required=False)
