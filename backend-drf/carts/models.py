from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from decimal import Decimal

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Total ammount of cart
    @property
    def subtotal(self):
        subtotal = Decimal('0.00')
        for item in self.items.all():
            subtotal += item.product.price * item.quantity
        return subtotal
    
    @property
    def tax_amount(self):
        tax = Decimal('0.00')
        for item in self.items.all():
            tax += (item.product.price * item.quantity) * Decimal(item.product.tax_percentage/Decimal("100.00"))
        return tax
    
    @property
    def grand_total(self):
        # grand_total = self.subtotal() + self.tax_amount()
        grand_total = self.subtotal + self.tax_amount # You can apply @property to run this line as telling as method
        return grand_total.quantize(Decimal("0.00"))

    def __str__(self):
        return self.user.email
    

class CartItem(models.Model):                                              # \|/ this items belongs to serilisers.py section
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items") # if you delete the cart, CartItem also deleted
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # here cartitem belongs to which product
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"  # Apple x 1
    
    @property
    def total_price(self):
        total_price = self.product.price * self.quantity
        return total_price