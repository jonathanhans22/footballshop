# models.py

from django.db import models

class Product(models.Model):
    # --- Definisikan pilihan kategori yang benar ---
    CATEGORY_CHOICES = [
        ('JERSEY', 'Jersey'),
        ('SHOES', 'Sepatu Bola'),
        ('BALL', 'Bola'),
        ('BOTTLE', 'botol'),
        ('', 'Pakaian Latihan'),
    ]

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    