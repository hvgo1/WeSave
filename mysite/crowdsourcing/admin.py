from django.contrib import admin
from crowdsourcing.models import Location,User,Individual,Group,Role,Campaign,WishType,Wishlist,User_Role,Campaign_User_Followers,Campaign_Wishlist

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ['barangay','city','country']
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','password','location']
class IndividualAdmin(admin.ModelAdmin):
    list_display = ['first_name','middle_name','last_name','birthday','user']
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name','user']
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['title','beneficiary_name','story','deadline','approval_tag','status','views','created_by']
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['name','wish_type']
class User_RoleAdmin(admin.ModelAdmin):
    list_display = ['user','role']
class Campaign_User_FollowersAdmin(admin.ModelAdmin):
    list_display = ['campaign','user']
class Campaign_WishlistAdmin(admin.ModelAdmin):
    list_display = ['campaign','wishlist','received_tag']

admin.site.register(Location,LocationAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Individual,IndividualAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Role)
admin.site.register(Campaign,CampaignAdmin)
admin.site.register(WishType)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(User_Role,User_RoleAdmin)
admin.site.register(Campaign_User_Followers,Campaign_User_FollowersAdmin)
admin.site.register(Campaign_Wishlist,Campaign_WishlistAdmin)
