from django.contrib import admin
from croedsourcing.models import UserProfile
from crowdsourcing.models import Country,Region,City,Barangay,Address,Service_Category,UserProfile,Individual,Group,Campaign,Wish,Keyword,Unregistered_Donor,Contact,Campaign_User_Followers,Campaign_User_Donor,Campaign_Wish,Campaign_Keyword
# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ['barangay','city','region','country']
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','address','photo']
class IndividualAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','middle_name','last_name','birthday']
class GroupAdmin(admin.ModelAdmin):
    list_display = ['user','name','service_category','registration_number']
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['title','beneficiary_name','deadline','status','views','created_by']
class WishAdmin(admin.ModelAdmin):
    list_display = ['name','wish_type']
class Unregistered_DonorAdmin(admin.ModelAdmin):
    list_display = ['name','campaign','amount']
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']
class Campaign_User_FollowersAdmin(admin.ModelAdmin):
    list_display = ['campaign','user']
class Campaign_User_DonorAdmin(admin.ModelAdmin):
    list_display = ['campaign','user','amount']
class Campaign_WishAdmin(admin.ModelAdmin):
    list_display = ['campaign','wish','completed','estimated_price']
class Campaign_Keyword(admin.ModelAdmin):
    list_display = ['campaign','keyword']

admin.site.register(City)
admin.site.register(Barangay)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Address,AddressAdmin)
admin.site.register(UserProfile,UserProfiledmin)
admin.site.register(Individual,IndividualAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Campaign,CampaignAdmin)
admin.site.register(Service_Category)
admin.site.register(Keyword)
admin.site.register(Wish,WishAdmin)
admin.site.register(Unregistered_Donor,Unregistered_DonorAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Campaign_User_Followers,Campaign_User_FollowersAdmin)
admin.site.register(Campaign_User_Donor,Campaign_User_DonorAdmin)
admin.site.register(Campaign_Wish,Campaign_WishAdmin)
admin.site.register(Campaign_Keyword,Campaign_KeywordAdmin)

