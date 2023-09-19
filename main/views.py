from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from django.urls import reverse
from django.core import serializers
from main.models import Product

# Create your views here.

status = ''

def show_default(request):
    global status
    status = ''
    context = {
        'name': 'Williams',
        'class' : 'PBP A',
    }
    return render(request, "default.html", context)

def show_main(request):
    products = Product.objects.all()
    total = 0
    for product in products:
        total += product.banyak

    context = {
        'products' : products,
        'status' : status,
        'total' : total
    }
    
    return render(request, "main.html", context)


def create_product(request):
    products = Product.objects.all()
    form = ProductForm(request.POST or None)

    name = request.POST.get('nama')
    banyak = request.POST.get('banyak')
    for product in products:
        if product.nama == name:
            product.banyak = product.banyak + int(request.POST.get('banyak'))
            product.save()
            global status
            status = f'Item {name} sudah ada di database, sehingga jumlahnya akan ditambahkan sebanyak {banyak} dan total dari {name} adalah {product.banyak}'
            return HttpResponseRedirect(reverse('main:show_main'))

    if form.is_valid() and request.method == "POST":
        form.save()
        status = f'Berhasil menambahkan item baru {name} sebanyak {banyak}'
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    global status
    status = ''
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    global status
    status = ''
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    global status
    status = ''
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    global status
    status = ''
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")