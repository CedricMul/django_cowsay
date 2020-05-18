from django import forms

class CowUserForm(forms.Form):
    say = forms.CharField(max_length=120)