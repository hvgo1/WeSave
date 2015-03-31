import datetime

from django.db import models
from django.utils import timezone

class Country(models.Model):
    def __unicode__(self):  
        return u'%s' %(self.name)
    name = models.CharField(max_length=200)

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

class Address(models.Model):
    def __unicode__(self):  
        return u'%s, %s, %s, %s, %s' %(self.street,self.barangay,self.city,self.region,self.country,self.street)    
    country = models.ForeignKey(Country)  
    region = models.ForeignKey(Region,null=True, blank=True)   
    city = models.ForeignKey(City,null=True, blank=True)    
    barangay = models.ForeignKey(Barangay,null=True, blank=True)
    street = models.CharField(max_length=200)

class Service_Category(models.Model):
    def __unicode__(self):  
        return u'%s' %(self.name)
    name = models.CharField(max_length=200)

class User(models.Model):
    def __unicode__(self): 
        return self.id
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=None, null=True, blank=True)
   

class Individual(models.Model):
    def __unicode__(self): 
        return u'%s,%s,%s' %(self.first_name,self.middle_name,self.last_name)#user
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200)
    birthday = models.DateTimeField('birthday')
    address = models.ForeignKey(Address)
    user = models.ForeignKey(User)

class Group(models.Model):
    def __unicode__(self): 
        return u'%s,%s' %(self.user,self.name)
    name = models.CharField(max_length=200)
    page_address = models.URLField(max_length=200,null=True, blank=True)
    about = models.CharField(max_length=200)
    service_category = models.ForeignKey(Service_Category)
    registration_number = models.BigIntegerField(null=True, blank=True)
    document = FileField(upload_to =None,null=True, blank=True)
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
    user = models.ForeignKey(User)

class Campaign(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.title)
    STATUS_CHOICES = (
        ('0', 'Draft'),
        ('1', 'For Approval'),
        ('2', 'Verified'),
        ('3', 'Completed'),
        ('4', 'Inactive'),
    )

    title = models.CharField(max_length=200)
    beneficiary_name = models.CharField(max_length=200)
    story = models.CharField(max_length=2000)
    deadline = models.DateTimeField('deadline')
    approval_tag = models.BooleanField()
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='0')#Draft
    views = models.BigIntegerField(default = 0)
    campaign_image = models.ImageField(upload_to=None, null=True, blank=True)
    created_by = models.ForeignKey(User)
    donors = models.ManyToManyField(User,through='Campaign_User_Donor',through_fields=('campaign', 'user'))
    subscribers = models.ManyToManyField(User,through='Campaign_User_Followers',through_fields=('campaign', 'user'))
   wishes = models.ManyToManyField(Wish,through='Campaign_Wish',through_fields=('campaign', 'wish'))
   keywords = models.ManyToManyField(Keyword,through='Campaign_Keywords',through_fields=('campaign', 'keyword'))
    # set default value of approval_tag to false

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

class Unregistered_Donor(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.name)
    name = models.CharField(max_length=200)
    campaign = models.ForeignKey(Campaign)
    amount = models.DecimalField(decimal_places=2)

class User_Role(models.Model):
    def __unicode__(self): 
        return u'%s,%s' %(self.user,self.role)
    STATUS_CHOICES = (
        ('Ben', 'Beneficiary'),
        ('Hos', 'Hospital_Rep'),
        ('Don', 'Donor'),
        ('Admin', 'Admin'),
    )
    user = models.ForeignKey(User)
    role = models.models.CharField(max_length=15,choices=STATUS_CHOICES)

class Campaign_User_Followers(models.Model):
    def __unicode__(self): 
        return u'%s,%s' %(self.campaign,self.user)
    campaign = models.ForeignKey(Campaign)
    user = models.ForeignKey(User)

class Campaign_User_Donor(models.Model):
    def __unicode__(self): 
        return u'%s,%s' %(self.campaign,self.user)
    campaign = models.ForeignKey(Campaign)
    user = models.ForeignKey(User)
    amount = models.DecimalField(decimal_places=2)

class Campaign_Wish(models.Model):
    def __unicode__(self): 
        return u'%s,%s,%s' %(self.campaign,self.wish,self.completed,self.estimated_price)
    campaign = models.ForeignKey(Campaign)
    wish = models.ForeignKey(Wish)
    completed = models.BooleanField()
    estimated_price = models.DecimalField(decimal_places=2)
    # set default value of received_tag to false

class Campaign_Keyword(models.Model):
    def __unicode__(self): 
        return u'%s,%s' %(self.campaign,self.wish,self.keyword)
    campaign = models.ForeignKey(Campaign)
    keyword = models.ForeignKey(Keyword)
   




