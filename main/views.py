from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login') # Wajib agar request.user selalu ada
def show_main(request):
    # 1. Ambil semua produk secara default
    product_list = Product.objects.all()
    
    # 2. Dapatkan nilai parameter 'filter' dari URL
    filter_type = request.GET.get('filter')
    
    # 3. Jika filter adalah 'my', ubah daftar produk
    if filter_type == 'my':
        # Ini adalah baris kunci:
        # Filter Product dimana field 'user' sama dengan pengguna yang sedang login
        product_list = Product.objects.filter(user=request.user)
        
    context = {
        'name': request.user.username,
        'npm' : "2406414025",
        'class' : "PBP B",
        'product_list': product_list,
        'active_filter': filter_type,
    }

    return render(request, "main.html", context)

@login_required(login_url='/login/')
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # 1. Tahan penyimpanan, jangan langsung ke database
            product = form.save(commit=False)
            
            # 2. Sisipkan data user yang sedang login ke dalam field 'user'
            product.user = request.user
            
            # 3. Sekarang simpan produk sepenuhnya ke database
            product.save()
            
            # Tambahkan pesan sukses (opsional tapi bagus)
            messages.success(request, 'Produk baru berhasil ditambahkan!')
            
            return redirect('main:show_main')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, "create_product.html", context)


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)
def show_xml(request):
    product_list = Product.objects.all()
    
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        Product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", Product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        Product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [Product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

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
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
                user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))