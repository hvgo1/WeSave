import datetime
import os

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.template.defaultfilters import slugify


class Region(models.Model):
    def __unicode__(self):  
        return u'%s' %(self.name)
    name = models.CharField(max_length=200) 

class City(models.Model):
    def __unicode__(self):  
        return u'%s' %(self.name)
    name = models.CharField(max_length=200)  

class Barangay(models.Model):
    def __unicode__(self):  
        return u'%s' %(self.name)
    name = models.CharField(max_length=200)

class Wish(models.Model):
    def __unicode__(self): 
        return u'%s,%s' %(self.name,self.wish_type)
    STATUS_CHOICES = (
        ('0', 'Cash'),
        ('1', 'In-Kind'),
    )
    name = models.CharField(max_length=200)
    wish_type = models.CharField(max_length=10,choices=STATUS_CHOICES)

class Keyword(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.name)
    name = models.CharField(max_length=200)

class Address(models.Model):
    def __unicode__(self):  
        return u'%s,%s,%s,%s,%s' %(self.street,self.barangay,self.city,self.region,self.country)    
 
    country = CountryField()
    region = models.ForeignKey(Region,null=True, blank=True)   
    city = models.ForeignKey(City,null=True, blank=True)    
    barangay = models.ForeignKey(Barangay,null=True, blank=True)
    street = models.CharField(max_length=200)

class ServiceCategory(models.Model):
    def __unicode__(self):  
        return u'%s' %(self.name)
    name = models.CharField(max_length=200)

class UserProfile(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.user.id)
    photo = models.ImageField(upload_to='profile_images/',null=True, blank=True)
    address = models.ForeignKey(Address)
    user = models.OneToOneField(User)
 
class UserRole(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.user.id)
    ROLE_CHOICES = (
        ('Soc', 'Social Worker'),
        ('Don', 'Donor'),
        ('Adm', 'WeSave Admin'),
    )
    
    user = models.ForeignKey(User,unique=True)
    role = models.CharField(max_length=25, choices=ROLE_CHOICES)

 #   class Meta:
  #      unique_together = ('user', 'role')

class Individual(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.user.id)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField('birthday')
    user = models.OneToOneField(User)

class Group(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.user.id)
    name = models.CharField(max_length=200)
    page_address = models.URLField(max_length=200,null=True, blank=True)
    about = models.CharField(max_length=200)
    service_category = models.ManyToManyField(ServiceCategory)
    registration_number = models.BigIntegerField(null=True, blank=True)
    document = models.FileField(upload_to ='documents/',null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    pc_first_name = models.CharField(max_length=200)
    pc_last_name = models.CharField(max_length=200)
    pc_email = models.EmailField(max_length=75)
    pc_job_title = models.CharField(max_length=200)
    pc_phone_number = models.CharField(max_length=12)
    sc_first_name = models.CharField(max_length=200)
    sc_last_name = models.CharField(max_length=200)
    sc_email = models.EmailField(max_length=75)
    sc_job_title = models.CharField(max_length=200)
    sc_phone_number = models.CharField(max_length=12)
    user = models.OneToOneField(User)

class Campaign(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Campaign, self).save(*args, **kwargs)

    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('F', 'For Approval'),
        ('A', 'Approved'),
        ('C', 'Completed'),
        ('I', 'Inactive'),
    )

    title = models.CharField(max_length=200)
    beneficiary_name = models.CharField(max_length=200)
    story = models.CharField(max_length=2000)
    deadline = models.DateTimeField('deadline')
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='D')#Draft
    views = models.BigIntegerField(default = 0)
    ack_receipt = models.ImageField(upload_to='ack_receipts/', null=True, blank=True)
    campaign_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    created_by = models.ForeignKey(User)
    donors = models.ManyToManyField(User,through='CampaignUserDonor',through_fields=('campaign','user'),related_name='campaign_donors')
    subscribers = models.ManyToManyField(User,through='CampaignUserFollowers',through_fields=('campaign', 'user'),related_name='campaign_subscribers')
    wishes = models.ManyToManyField(Wish,through='CampaignWish')
    keywords = models.ManyToManyField(Keyword,through='CampaignKeyword')
    slug = models.SlugField(unique = True)

class UnregisteredDonor(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.name)
    name = models.CharField(max_length=200)
    campaign = models.ForeignKey(Campaign)
    amount = models.DecimalField(max_digits=20,decimal_places=2)

class Contact(models.Model):
    def __unicode__(self): 
        return u'%s,%s,%s,%s' %(self.name,self.email,self.message,self.status)
    STATUS_CHOICES = (
        ('R', 'Read'),
        ('U', 'Unread'),
    )    
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=75)
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='U')#Draft

class CampaignUserDonor(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.id)
    campaign = models.ForeignKey(Campaign)
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=20,decimal_places=2)

class CampaignWish(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.id)
    campaign = models.ForeignKey(Campaign)
    wish = models.ForeignKey(Wish)
    completed = models.BooleanField()
    estimated_price = models.DecimalField(max_digits=20,decimal_places=2)
    # set default value of received_tag to false

class CampaignUserFollowers(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.id)
    campaign = models.ForeignKey(Campaign)
    user = models.ForeignKey(User)

class CampaignKeyword(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.id)
    campaign = models.ForeignKey(Campaign)
    keyword = models.ForeignKey(Keyword)
 

