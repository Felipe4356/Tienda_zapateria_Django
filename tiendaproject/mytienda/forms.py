from django import forms
from .models import CarritoProducto,Contacto

class CarritoProductoForm(forms.ModelForm):
    class Meta:
        model = CarritoProducto
        fields = ['producto', 'cantidad']





class CantidadProductoForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1, initial=1, label='Cantidad')



class ContactoForm(forms.ModelForm):
  
    class Meta:
        
        model = Contacto
       
        fields = ['nombre', 'email', 'mensaje']
      
        widgets = {
           
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
         
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
      
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }