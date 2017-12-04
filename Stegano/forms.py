from django import forms

from .models import SaveInfo


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = SaveInfo
        fields = ("input_msg", "input_key", "input_img")