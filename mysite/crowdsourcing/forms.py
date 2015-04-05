from django import forms
from django_countries.widgets import CountrySelectWidget
from crowdsourcing.models import Individual, Group, UserProfile, Address

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user','address']

class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ("first_name", "middle_name", "last_name","birthday")   

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("name", "page_address", "about","service_category",
        "registration_number","document","comments","pc_first_name",
        "pc_last_name","pc_email","pc_job_title","sc_phone_number")  

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("country","region","city","barangay","street")
        widgets = {'country': CountrySelectWidget()}
