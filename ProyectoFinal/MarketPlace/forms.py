from django import forms

class VehiculoFormulario(forms.Form):
    marca=forms.CharField()
    modelo=forms.CharField()
    año=forms.IntegerField()
    
class CategoriaFormulario (forms.Form):
    tipo_vehiculo=forms.CharField()
    combustible=forms.CharField()
    cilindrada_motor=forms.CharField()
    
class VendedorFormulario(forms.Form):
    nombre=forms.CharField()
    telefono=forms.IntegerField()
    correo=forms.EmailField()