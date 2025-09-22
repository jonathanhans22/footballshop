# models.py
import uuid  
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # --- Definisikan pilihan kategori yang benar ---
    CATEGORY_CHOICES = [
        ('JERSEY', 'Jersey'),
        ('SHOES', 'Sepatu Bola'),
        ('BALL', 'Bola'),
        ('BOTTLE', 'botol'),
        ('TRAINING KIT', 'Pakaian Latihan'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.name