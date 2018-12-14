from .models import Cliente
from django import forms
from accounts.models import User

class registrarCliente(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('nombre', 'direccion', 'ciudad', 'comuna', 'telefono', 'correo', )


class asignarTecnico(forms.Form):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    cliente = forms.ModelChoiceField(queryset = Cliente.objects.all())

