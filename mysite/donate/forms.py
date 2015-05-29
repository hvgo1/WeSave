from django import forms
from donate.models import InkindDonation

class InkindForm1(forms.ModelForm):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=128)
    address = forms.CharField(max_length=128)
    pc_contact_number = forms.CharField(max_length=128,label="Primary Contact Number")
    sc_contact_number = forms.CharField(max_length=128,label="Secondary Contact Number")
    description = forms.CharField(widget=forms.Textarea,help_text = "Please input a description of your donation.")
    reason = forms.CharField(widget=forms.Textarea,help_text = "Please input a reason for your donation.")
    fair_market_value = forms.DecimalField(widget=TextInput(attrs={'type':'number'}),max_digits=20,decimal_places=2)
    class Meta:
        model = InkindDonation
        exclude = ('campaign',)
        fields = ('name','email','address','pc_contact_number','sc_contact_number','description','reason','fair_market_value')

class InkindForm2(forms.ModelForm):
    
    sc_contact_number = forms.CharField(max_length=128,label="Secondary Contact Number")
    description = forms.CharField(widget=forms.Textarea,help_text = "Please input a description of your donation.")
    reason = forms.CharField(widget=forms.Textarea,help_text = "Please input a reason for your donation.")
    fair_market_value = forms.DecimalField(widget=TextInput(attrs={'type':'number'}),max_digits=20,decimal_places=2)
    class Meta:
        model = InkindDonation
        exclude = ('campaign',)
        fields = ('sc_contact_number','description','reason','fair_market_value')

class InkindForm3(forms.ModelForm):
    
    description = forms.CharField(widget=forms.Textarea,help_text = "Please input a description of your donation.")
    reason = forms.CharField(widget=forms.Textarea,help_text = "Please input a reason for your donation.")
    fair_market_value = forms.DecimalField(widget=TextInput(attrs={'type':'number'}),max_digits=20,decimal_places=2)
    class Meta:
        model = InkindDonation
        exclude = ('campaign',)
        fields = ('description','reason','fair_market_value')