from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    unit_price = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    PAYMENT_PENDING = 'Pending'
    PAYMENT_DELIVERED = 'Delivered'
    PAYMENT_CANCELLED = 'Cancelled'
    PAYMENT_STATUS = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_DELIVERED, 'Delivered'),
        (PAYMENT_CANCELLED, 'Cancelled'),
    ]
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    payment_status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS, default=PAYMENT_PENDING)
    placed_at = models.DateField(auto_now_add=True, null=True)

    @property
    def total_amount(self):
        return self.order_quantity*self.name.unit_price

    def __str__(self):
        return f'{self.name} ordered by {self.customer}'

