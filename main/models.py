from django.db import models

# Create your models here.
class Shop(models.Model):
    CATEGORY_CHOICES = [
        ('name ', 'Name'),
        ('price ', 'Price '),
        ('description ', 'Description '),
        ('thumbnail ', 'Thumbnail '),
        ('category', 'Category'),
        ('is_featured', 'Is_Featured'),
        ('brand', 'Brand')
    ]

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=100)