from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["nama", "banyak", "deskripsi", "harga", "jenis"]