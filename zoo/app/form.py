from django.forms import ModelForm
from app.models import Cadastro

# Create the form class.
class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'usuario', 'senha', 'confirmarsenha']