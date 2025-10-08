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
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    form = ProductForm() # Buat instance form kosong
    context = {
        'name': request.user.username,
        'npm' : "2406414025",
        'class' : "PBP B",
        'form': form, # Tambahkan form ke context
    }
    return render(request, "main.html", context)

@csrf_exempt # Atau gunakan metode lain untuk menangani CSRF token di AJAX
@login_required(login_url='/login/')
def create_product_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            # Kembalikan respons JSON sebagai konfirmasi
            return JsonResponse({"status": "success", "message": "Produk berhasil ditambahkan!"}, status=201)
        else:
            # Kembalikan error validasi jika form tidak valid
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


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
    # HAPUS KODE LAMA DAN GANTI DENGAN INI:
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
    """
    Mengambil satu data produk berdasarkan ID dan mengembalikannya dalam format JSON.
    """
    try:
        product = Product.objects.select_related('user').get(pk=product_id)

        # --- LOGIKA BARU UNTUK THUMBNAIL ---
        thumbnail_url = None
        if product.thumbnail:
            # Cek apakah thumbnail adalah objek file (punya .url) atau sudah berupa string
            if hasattr(product.thumbnail, 'url'):
                thumbnail_url = product.thumbnail.url
            else:
                # Jika sudah berupa string, anggap itu adalah URL/path-nya
                thumbnail_url = str(product.thumbnail)
        # ------------------------------------

        data = {
            'pk': str(product.pk),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.get_category_display(),
            'thumbnail': thumbnail_url,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Produk tidak ditemukan'}, status=404)

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

@csrf_exempt
@login_required(login_url='/login/')
def edit_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        # Pastikan user yang mengedit adalah pemilik produk
        if product.user != request.user:
            return JsonResponse({"status": "error", "message": "Anda tidak berhak mengedit produk ini."}, status=403)
            
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Produk berhasil diperbarui!"})
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
@login_required(login_url='/login/')
def delete_product_ajax(request, id):
    if request.method == 'POST': # Sebaiknya gunakan POST untuk aksi yang mengubah data
        try:
            product = Product.objects.get(pk=id)
            # Pastikan user yang menghapus adalah pemilik produk
            if product.user != request.user:
                return JsonResponse({"status": "error", "message": "Anda tidak berhak menghapus produk ini."}, status=403)
            
            product.delete()
            return JsonResponse({"status": "success", "message": "Produk berhasil dihapus."})
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Produk tidak ditemukan."}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)