from django import forms
from Collections.models import AlbumModel


class ImageForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'