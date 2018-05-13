from django import forms
from .models import Zapisy

class ZapisyForm(forms.ModelForm):
    class Meta:
        model = Zapisy
        fields = [
            "your_choice",
            "hour_choice",
            "day_choice"
        ]
