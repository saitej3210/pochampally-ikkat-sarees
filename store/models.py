from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('SAREE', 'Saree'),
        ('DRESS', 'Dress Material'),
        ('FABRIC', 'Fabric / Cloth'),
    ]

    FABRIC_CHOICES = [
        ('PATTU', 'Pattu Silk'),
        ('SILK', 'Silk'),
        ('COTTON', 'Cotton'),
        ('MIX', 'Mix Fabric'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    fabric = models.CharField(max_length=10, choices=FABRIC_CHOICES, default='OTHER')
    color = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
