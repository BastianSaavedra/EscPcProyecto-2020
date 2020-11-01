from django import forms
from django.forms import ModelForm
from .models import PlacasMadre, Procesadore ,Contacto

class PlacaForm(ModelForm):
    class Meta:
        model = PlacasMadre
        fields = ['marca','modelo','formato','plataforma','stock','imagen','imagen_detail','precio']

class ProceForm(ModelForm):
    class Meta:
        model = Procesadore
        fields = ['marca','modelo','frecuencia','socket','stock','imagen','imagen_detail','precio']

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
