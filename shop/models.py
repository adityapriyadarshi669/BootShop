from django.db import models

# Create your models here.


class Product(models.Model):
    itemName = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    size = models.IntegerField()

    def __str__(self):
        return self.itemName


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Cquantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.itemName}:{self.Cquantity}"


class Cart(models.Model):
    items = models.ManyToManyField(CartProduct, blank=True)


class Transaction(models.Model):
    user = models.CharField(max_length=255, default="Anonymous")
    cartItems = models.ManyToManyField(CartProduct, blank=True)

    def __str__(self):
        return f"Transaction ID:{self.id}"
