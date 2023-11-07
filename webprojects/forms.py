from django.forms import ModelForm

from webprojects.models import Client, Product, Transaction

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

        
