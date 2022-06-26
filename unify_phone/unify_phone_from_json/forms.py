from django import forms


class PhoneForm(forms.Form):
    phone = forms.CharField(max_length=100, required=True)