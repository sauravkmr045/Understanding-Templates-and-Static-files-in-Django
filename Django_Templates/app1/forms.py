from django import forms

class myform(forms.Form):
    first_name = forms.CharField(max_length = 250)
    last_name = forms.CharField(max_length =250)
    email = forms.CharField (max_length =250)
    comment = forms.CharField(widget = forms.Textarea)
