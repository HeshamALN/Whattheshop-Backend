from django.db import models
from django.contrib.auth.models import User


class Salfa(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    description = models.TextField()
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    img = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.name

# class FavoriteSalfa(models.Model):
#     salfa = models.ForeignKey(Salfa, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	salfa = models.ManyToManyField(Salfa, through="CartSalfa")


class CartSalfa(models.Model):
	salfa = models.ForeignKey(Salfa, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
