from django import forms
from django_countries.widgets import CountrySelectWidget
from crowdsourcing.models import Individual, Group, UserProfile
from django.contrib.auth.models import User

#Form for UserProfile model
class UserProfileForm(forms.ModelForm): 
    class Meta:
        model = UserProfile
        fields = ("photo","country","region","city","barangay","street")
        widgets = {'country': CountrySelectWidget()}
        

#Form for Individual model
class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ("first_name", "middle_name", "last_name","birthday")   

#Form for Group model
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("name", "page_address", "about","service_category",
        "registration_number","document","comments","pc_first_name",
        "pc_last_name","pc_email","pc_job_title","pc_phone_number",
        "sc_first_name","sc_last_name","sc_email","sc_job_title","sc_phone_number")  

