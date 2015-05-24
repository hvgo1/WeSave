from django.contrib import admin
from django.contrib.auth.models import User
from crowdsourcing.models import Region,City,Barangay,Wish,Keyword,Address,ServiceCategory, UserProfile,Individual,Group,Campaign,CampaignUserDonor,CampaignUserFollowers, CampaignKeyword,UnregisteredDonor,CampaignWish,UserRole
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
    list_display = ['id','user','name','getServiceCategory','registration_number']
    def getServiceCategory(self, obj):
        return ",".join([var.name for var in obj.service_category.all()])
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['id','title','beneficiary_name','deadline','status','views','campaign_image','created_by']

class CampaignUserDonorAdmin(admin.ModelAdmin):
    list_display = ['id','campaign','user','amount']

class CampaignUserFollowersAdmin(admin.ModelAdmin):
    list_display = ['id','campaign','user']

class CampaignKeywordAdmin(admin.ModelAdmin):
    list_display = ['id','campaign','keyword']

class UnregisteredDonorAdmin(admin.ModelAdmin):
    list_display = ['id','name','campaign','amount']

class CampaignWishAdmin(admin.ModelAdmin):
    list_display = ['id','campaign','wish','completed','estimated_price']

class CityAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class BarangayAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class RegionAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(City,CityAdmin)
admin.site.register(Barangay,BarangayAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Wish,WishAdmin)
admin.site.register(Keyword,KeywordAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(ServiceCategory,ServiceCategoryAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserRole,UserRoleAdmin)
admin.site.register(Individual,IndividualAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Campaign,CampaignAdmin)
admin.site.register(CampaignUserDonor,CampaignUserDonorAdmin)
admin.site.register(CampaignUserFollowers,CampaignUserFollowersAdmin)
admin.site.register(CampaignKeyword,CampaignKeywordAdmin)
admin.site.register(UnregisteredDonor,UnregisteredDonorAdmin)
admin.site.register(CampaignWish,CampaignWishAdmin)
