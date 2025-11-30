from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    quantity_in_stock = models.IntegerField()
    reorder_point = models.IntegerField()
    active = models.BooleanField(default=True)
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Product'