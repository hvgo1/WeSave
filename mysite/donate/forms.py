from django import forms
from donate.models import InkindDonation
from crowdsourcing.models import CampaignUserDonor

class InkindForm1(forms.ModelForm):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=128)
    address = forms.CharField(max_length=128)
    pc_contact_number = forms.CharField(max_length=128,label="Primary Contact Number")
    sc_contact_number = forms.CharField(max_length=128,label="Secondary Contact Number")
    description = forms.CharField(widget=forms.Textarea,help_text = "Please input a description of your donation.")
    remarks = forms.CharField(widget=forms.Textarea,help_text = "Please input some remarks.")
    fair_market_value = forms.DecimalField(max_digits=20,decimal_places=2)
    class Meta:
        model = InkindDonation
        exclude = ('campaign',)
        fields = ('name','email','address','pc_contact_number','sc_contact_number','description','remarks','fair_market_value')

class InkindForm2(forms.ModelForm):
    
    sc_contact_number = forms.CharField(max_length=128,label="Secondary Contact Number")
    description = forms.CharField(widget=forms.Textarea,help_text = "Please input a description of your donation.")
    remarks = forms.CharField(widget=forms.Textarea,help_text = "Please input a remarks for your donation.")
    fair_market_value = forms.DecimalField(max_digits=20,decimal_places=2)
    class Meta:
        model = InkindDonation
        exclude = ('campaign',)
        fields = ('sc_contact_number','description','remarks','fair_market_value')

class InkindForm3(forms.ModelForm):
    
    description = forms.CharField(widget=forms.Textarea,help_text = "Please input a description of your donation.")
    remarks = forms.CharField(widget=forms.Textarea,help_text = "Please input some remarks.")
    fair_market_value = forms.DecimalField(max_digits=20,decimal_places=2)
    class Meta:
        model = InkindDonation
        exclude = ('campaign',)
        fields = ('description','remarks','fair_market_value')

class CampaignUserDonorForm(forms.ModelForm):
    class Meta:
        model = CampaignUserDonor
        fields = ('user', 'amount')
