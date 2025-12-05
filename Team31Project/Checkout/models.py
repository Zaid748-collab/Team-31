from django.conf import settings
from django.db import models
from Product_List.models import Product 


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="checkout_orders" 
    )
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items" 
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="checkout_orderitems" 
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x{self.quantity} (Order {self.order.id})"
