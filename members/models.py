from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from core.models import Product, Color, Size


class Member(models.Model):
    """A member (customer) that can sign up to store their address for faster checkout."""
    # Profile Model: we use the Member class to add some additional information to
    # the built-in django User model.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = PhoneNumberField(blank=True)
    address_street1 = models.CharField(max_length=255)
    address_street2 = models.CharField(max_length=255, blank=True)
    address_suburb = models.CharField(max_length=255)
    address_state = models.CharField(max_length=255)
    address_country = models.CharField(max_length=255)
    address_postcode = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    """Represents an item "saved" in a Member's cart, and allows us to load all items into the
    session when a user logs in, to restore their cart."""
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    session_item_id = models.UUIDField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()




class WishlistItem(models.Model):
    """Represents an item "saved" in a Member's cart, and allows us to load all items into the
    session when a user logs in, to restore their cart."""
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    session_item_id = models.UUIDField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()