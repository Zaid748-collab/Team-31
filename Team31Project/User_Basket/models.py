from django.db import models

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()

    class Meta:
        db_table = 'cart'

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        db_table = 'cartitem'