from django.contrib import admin
from donate.models import InkindDonation


class InkindAdmin(admin.ModelAdmin):
    list_display = ['name','email','address','pc_contact_number','sc_contact_number','description','remarks','fair_market_value','campaign']

admin.site.register(InkindDonation,InkindAdmin)