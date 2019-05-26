from django import forms
from .models import sells


class SellForm(forms.ModelForm):

    class Meta:
        model = sells
        fields = ('client', 'stock', 'transaction_date')