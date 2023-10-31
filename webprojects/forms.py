from django.forms import ModelForm

from webprojects.models import Client, Product, Transaction

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '_all_'