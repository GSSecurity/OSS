from django import forms

from .models import SaveInfo


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = SaveInfo
        fields = ("user_ip", "user_plain_text", "user_agent", "user_file")

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)