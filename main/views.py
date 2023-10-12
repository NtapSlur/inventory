from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from django.urls import reverse
from django.core import serializers
from main.models import Product
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    total = 0
    for product in products:
        total += product.banyak

    context = {
        'name': request.user.username,
        'products' : products,
        'status' : status,
        'total' : total,
        'last_login': request.COOKIES['last_login'],
        'strip' : '-' * (len(request.user.username) + 20),

    }
    
    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    name = str(request.POST.get('nama'))
    banyak = request.POST.get('banyak')
    products = Product.objects.filter(user=request.user)
    for product in products:
        if product.nama.lower() == name.lower():
            global status
            status = f'Gagal menambahkan {name}, {name} sudah ada di Database'
            return HttpResponseRedirect(reverse('main:show_main'))

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    total = 0
    for product in product_item:
        total += product.banyak
    data = {
        'products': serializers.serialize('json', product_item),
        'total': total,
        'status':status,
    }
    return JsonResponse(data)

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        nama = request.POST.get("nama")
        harga = request.POST.get("harga")
        deskripsi = request.POST.get("deskripsi")
        banyak = request.POST.get("banyak")
        jenis = request.POST.get("jenis")
        user = request.user
        for product in Product.objects.filter(user=request.user):
            if product.nama.lower() == nama.lower():
                global status
                status = f'Gagal menambahkan {nama}, {nama} sudah ada di Database'
                products = Product.objects.filter(user=request.user)
                total = 0
                for product in products:
                    total += product.banyak
                return JsonResponse({'status': status, 'total': total}, status=201)
        new_product = Product(nama=nama, harga=harga, deskripsi=deskripsi, banyak = banyak, jenis=jenis, user=user)
        new_product.save()

        status = f'Berhasil menambahkan item baru {nama} sebanyak {banyak}'
        for product in products:
            total += product.banyak

        return JsonResponse({'status': status, 'total': total}, status=201)

    return HttpResponseNotFound()

