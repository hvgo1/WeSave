from django.db import models
from crowdsourcing.models import Campaign

class InkindDonation(models.Model):
    def __unicode__(self):  
        return u'%s,%s' %(self.name,self.email)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=128)
    address = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    pc_contact_number = models.CharField(max_length=128)
    sc_contact_number = models.CharField(max_length=128)
    description = models.CharField(max_length=1200)
    reason = models.CharField(max_length=1200)
    fair_market_value = models.DecimalField(max_digits=20,decimal_places=2)
    campaign = models.ForeignKey(Campaign)    