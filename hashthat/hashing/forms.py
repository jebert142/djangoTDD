from django import forms

class HashForm(forms.Form):
    text = forms.CharField(label='Enter Hash Here', max_length=500, widget=forms.Textarea)