from django import forms
from crowdsourcing.models import Individual, Group, UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("photo", "address", "user","role")
        
class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ("first_name", "middle_name", "last_name","birthday")   

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("name", "page_address", "about","service_category","registration_number","document","comments","pc_first_name","pc_last_name","pc_email","pc_job_title","sc_phone_number")  

