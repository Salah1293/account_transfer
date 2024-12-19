from django import forms
from .models import *


class UploadForm(forms.Form):
    document = forms.FileField()



class TransferFundsForm(forms.Form):
    source_account = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        label="From Account",
        required=True,
        widget=forms.Select,
        empty_label="Select Source Account"
    )
    target_account = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        label="To Account",
        required=True,
        widget=forms.Select,
        empty_label="Select Target Account"
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Amount",
        required=True,
        min_value=0.01
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['source_account'].label_from_instance = lambda obj: obj.name
        self.fields['target_account'].label_from_instance = lambda obj: obj.name


