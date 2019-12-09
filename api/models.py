from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify




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
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="carts" )
    salfa = models.ManyToManyField(Salfa, through="CartSalfa")
    checkout_status = models.BooleanField(default= False)


class CartSalfa(models.Model):
    salfa = models.ForeignKey(Salfa, on_delete=models.CASCADE, related_name="cart_salfa")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_salfa")


@receiver(post_save, sender=CartSalfa)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)









