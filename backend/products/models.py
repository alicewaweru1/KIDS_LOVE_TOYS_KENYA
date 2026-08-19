from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("toys", "Toys"),
        ("dolls", "Dolls"),
        ("cars", "Cars"),
        ("educational", "Educational"),
        ("outdoor", "Outdoor"),
        ("games", "Games"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
