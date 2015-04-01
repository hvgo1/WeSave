from django.contrib import admin

from crowdsourcing.models import Country,Region,City,Barangay,Wish,Keyword,Address,Service_Category,UserProfile,Individual,Group,Campaign,Campaign_User_Donor,Campaign_User_Followers,Campaign_Keyword,Unregistered_Donor,Contact,Campaign_Wish
# Register your models here.
 
class WishAdmin(admin.ModelAdmin):
    list_display = ['name','wish_type']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['street','barangay','city','region','country']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','address','photo']

class IndividualAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','middle_name','last_name','birthday']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['user','name','service_category','registration_number']

class CampaignAdmin(admin.ModelAdmin):
    list_display = ['title','beneficiary_name','deadline','status','views','created_by']

class Campaign_User_DonorAdmin(admin.ModelAdmin):
    list_display = ['campaign','user','amount']

class Campaign_User_FollowersAdmin(admin.ModelAdmin):
    list_display = ['campaign','user']

class Campaign_KeywordAdmin(admin.ModelAdmin):
    list_display = ['campaign','keyword']

class Unregistered_DonorAdmin(admin.ModelAdmin):
    list_display = ['name','campaign','amount']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']

class Campaign_WishAdmin(admin.ModelAdmin):
    list_display = ['campaign','wish','completed','estimated_price']



admin.site.register(City)
admin.site.register(Barangay)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Wish,WishAdmin)
admin.site.register(Keyword)
admin.site.register(Address,AddressAdmin)
admin.site.register(Service_Category)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Individual,IndividualAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Campaign,CampaignAdmin)
admin.site.register(Campaign_User_Donor,Campaign_User_DonorAdmin)
admin.site.register(Campaign_User_Followers,Campaign_User_FollowersAdmin)
admin.site.register(Campaign_Keyword,Campaign_KeywordAdmin)
admin.site.register(Unregistered_Donor,Unregistered_DonorAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Campaign_Wish,Campaign_WishAdmin)
