import datetime

from django.db import models
from django.utils import timezone

class Location(models.Model):
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    barangay = models.CharField(max_length=200)

class User(models.Model):
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=None, null=True, blank=True)
    location = models.ForeignKey(Location)

class Individual(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateTimeField('birthday')
    user = models.ForeignKey(User)

class Group(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)

class Role(models.Model):
    name = models.CharField(max_length=200)

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    beneficiary_name = models.CharField(max_length=200)
    story = models.CharField(max_length=2000)
    deadline = models.DateTimeField('deadline')
    approval_tag = models.BooleanField()
    status = models.IntegerField()
    views = models.BigIntegerField()
    created_by = models.ForeignKey(User)
    # set default value of approval_tag to false

class WishType(models.Model):
    name = models.CharField(max_length=200)

class Wishlist(models.Model):
    name = models.CharField(max_length=200)
    wish_type = models.ForeignKey(WishType)

class User_Role(models.Model):
    user = models.ForeignKey(User)
    role = models.ForeignKey(Role)

class Campaign_User_Followers(models.Model):
    campaign = models.ForeignKey(Campaign)
    user = models.ForeignKey(User)

class Campaign_Wishlist(models.Model):
    campaign = models.ForeignKey(Campaign)
    wishlist = models.ForeignKey(Wishlist)
    received_tag = models.BooleanField()
    # set default value of received_tag to false

