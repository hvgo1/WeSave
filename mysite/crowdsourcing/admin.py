from django.contrib import admin
from django.contrib.auth.models import User
from crowdsourcing.models import Region,City,Barangay,Wish,Keyword,Address,Service_Category, UserProfile,Individual,Group,Campaign,Campaign_User_Donor,Campaign_User_Followers, Campaign_Keyword,Unregistered_Donor,Contact,Campaign_Wish,User_Role
# Register your models here.

 
class WishAdmin(admin.ModelAdmin):
    list_display = ['id','name','wish_type']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','street','barangay','city','region','country']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','address','photo']

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['id','user','role']

class IndividualAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','middle_name','last_name','birthday']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','get_servicecat','registration_number']
    def get_servicecat(self, obj):
        return ",".join([p.name for p in obj.service_category.all()])
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['id','title','beneficiary_name','deadline','status','views','created_by']

class Campaign_User_DonorAdmin(admin.ModelAdmin):
    list_display = ['id','campaign','user','amount']

class Campaign_User_FollowersAdmin(admin.ModelAdmin):
    list_display = ['id','campaign','user']

class Campaign_KeywordAdmin(admin.ModelAdmin):
    list_display = ['id','campaign','keyword']

class Unregistered_DonorAdmin(admin.ModelAdmin):
    list_display = ['id','name','campaign','amount']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']

class Campaign_WishAdmin(admin.ModelAdmin):
    list_display = ['id','campaign','wish','completed','estimated_price']

class CityAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class BarangayAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class RegionAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class Service_CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(City,CityAdmin)
admin.site.register(Barangay,BarangayAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Wish,WishAdmin)
admin.site.register(Keyword,KeywordAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Service_Category,Service_CategoryAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(User_Role,UserRoleAdmin)
admin.site.register(Individual,IndividualAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Campaign,CampaignAdmin)
admin.site.register(Campaign_User_Donor,Campaign_User_DonorAdmin)
admin.site.register(Campaign_User_Followers,Campaign_User_FollowersAdmin)
admin.site.register(Campaign_Keyword,Campaign_KeywordAdmin)
admin.site.register(Unregistered_Donor,Unregistered_DonorAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Campaign_Wish,Campaign_WishAdmin)
