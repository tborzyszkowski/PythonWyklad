from django import forms


class ImageForm(forms.Form):
    image = forms.FileField(
        label='Wybierz plik'
    )