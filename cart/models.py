from django.db import models
from mycoffee.models import Coffee
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

class CartItem(models.Model):
    cart = models.ForeignKey("Cart")
    item = models.ForeignKey(Coffee)
    quantity = models.PositiveIntegerField(default=1)
    line_item_total = models.DecimalField(decimal_places = 3, max_digits = 20)

    def __str__(self):
        return self.item.title


def cart_item_pre_save(instance, *args, **kwargs):
	if qty >= 1:
		price = instance.item.price
		total = price * qty
		instance.line_item_total = total
	pre_save.connect(cart_item_pre_sace,sender=CartItem)

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    items = models.ManyToManyField(Coffee, through=CartItem)
    subtotal = models.DecimalField(decimal_places = 3, max_digits = 50, default=2.000)
    delivery_total = models.DecimalField(decimal_places = 3, max_digits = 50, default=2.000)
    total = models.DecimalField(decimal_places = 3, max_digits = 50, default=2.000)

    def __str__(self):
        return str(self.id)

       	def __str__(self):
        	return str(self.id)

    def update_subtotal(self):
        subtotal = 0
        items = self.cartitem_set.all()
        for item in items:
            subtotal += item.line_item_total
        self.subtotal = "%.3f"%subtotal
        self.save()


def do_delivery_and_total(sender, instance, *args, **kwargs):
    	subtotal = Decimal(instance.subtotal)
    	delivery_total = Decimal(2.000)
    	total = subtotal + delivery_total
    	instance.delivery_total = "%.3f"%delivery_total
    	instance.total = "%.3f"%total

pre_save.connect(do_delivery_and_total, sender=Cart)
