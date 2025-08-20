from django import forms

class FormIMC(forms.Form):
    peso = forms.FloatField(label='Peso')
    altura = forms.FloatField(label='altura')