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

class UserProfile(models.Model):
    def __unicode__(self): 
        return self.user.id
     STATUS_CHOICES = (
        ('Ben', 'Beneficiary'),
        ('Hos', 'Hospital_Rep'),
        ('Don', 'Donor'),
        ('Adm', 'Admin'),
    )
    photo = models.ImageField(upload_to=, null=True, blank=True)
    address = models.ForeignKey(Address)
    user = models.OneToOneField(User)
    role = models.models.CharField(max_length=15,choices=STATUS_CHOICES)

   

class Individual(models.Model):
    def __unicode__(self): 
        return u'%s,%s,%s' %(self.first_name,self.middle_name,self.last_name)#user
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200)
    birthday = models.DateTimeField('birthday')
    user = models.OneToOneField(User)

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
    user = models.OneToOneField(User)

class Campaign(models.Model):
    def __unicode__(self): 
        return u'%s' %(self.title)
    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('F', 'For Approval'),
        ('V', 'Verified'),
        ('C', 'Completed'),
        ('I', 'Inactive'),
    )

    title = models.CharField(max_length=200)
    beneficiary_name = models.CharField(max_length=200)
    story = models.CharField(max_length=2000)
    deadline = models.DateTimeField('deadline')
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='D')#Draft
    views = models.BigIntegerField(default = 0)
    ack_receipt = models.ImageField(upload_to=None, null=True, blank=True)
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

class Contact(models.Model):
    def __unicode__(self): 
        return u'%s,%s,%s' %(self.name,self.email,self.message)
    name = models.CharField(max_length=200)
    email = models.models.EmailField(max_length=75)
    message = models.CharField(max_length=200)

class Campaign_User_Followers(models.Model):
    def __unicode__(self): 
        return u'%s,%s' %(self.campaign,self.user)
    campaign = models.ForeignKey(Campaign)
    user = models.ForeignKey(User)

class Campaign_User_Donor(models.Model):
    def __unicode__(self): 
        return u'%s,%s,%s' %(self.campaign,self.user,self.amount)
    campaign = models.ForeignKey(Campaign)
    user = models.ForeignKey(User)
    amount = models.DecimalField(decimal_places=2)

class Campaign_Wish(models.Model):
    def __unicode__(self): 
        return u'%s,%s,%s,%s' %(self.campaign,self.wish,self.completed,self.estimated_price)
    campaign = models.ForeignKey(Campaign)
    wish = models.ForeignKey(Wish)
    completed = models.BooleanField()
    estimated_price = models.DecimalField(decimal_places=2)
    # set default value of received_tag to false

class Campaign_Keyword(models.Model):
    def __unicode__(self): 
        return u'%s,%s' %(self.campaign,self.keyword)
    campaign = models.ForeignKey(Campaign)
    keyword = models.ForeignKey(Keyword)
   




