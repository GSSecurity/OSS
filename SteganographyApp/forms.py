from django import forms

from SteganographyApp import UploadFileModel


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file')
