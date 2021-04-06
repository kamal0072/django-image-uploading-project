from django import forms
from .models import UserImage

class Userforms(forms.ModelForm):
    class Meta:
        model=UserImage
        fields='__all__'
        labels={'pics':'Choose Image:'}
