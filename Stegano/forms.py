from django import forms

from .models import SaveInfo


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = SaveInfo
        fields = ("input_msg", "input_key", "input_img")

class ExtractFileForm(forms.ModelForm):
    class Meta:
    	    model = SaveInfo
    	    fields = ("input_img", "input_key")