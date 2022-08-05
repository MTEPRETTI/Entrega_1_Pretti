from django import forms

class AppFormularios(forms.Form):

    rsoc = forms.CharField()
    zona = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()

class BusqFormulario(forms.Form):
    rsoc = forms.CharField()