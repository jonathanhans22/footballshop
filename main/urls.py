# urls.py

from django.urls import path
# Pastikan semua view yang dibutuhkan sudah diimpor
from main.views import (
    show_main, create_product_ajax, show_product, show_xml, 
    show_json, show_xml_by_id, show_json_by_id, register, 
    login_user, logout_user, edit_product_ajax, delete_product_ajax
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    
    # URL untuk halaman (jika masih ada, seperti halaman detail non-AJAX)
    path('product/<uuid:id>/', show_product, name='show_product'), 
    
    # URL untuk JSON (API Endpoints)
    path('json/', show_json, name='show_json'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    
    # URL untuk XML
    path('xml/', show_xml, name='show_xml'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'), 
    
    # URL untuk Autentikasi
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    
    # URL untuk AJAX CRUD
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'), # <-- PERBAIKAN DI SINI
    path('delete-product-ajax/<uuid:id>/', delete_product_ajax, name='delete_product_ajax'), # <-- PERBAIKAN DI SINI
]