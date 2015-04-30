from django import forms

from crowdsourcing.models import Contact

#Form for contact model
class ContactForm(forms.ModelForm): 
    class Meta:
        model = Contact
        fields = ('name','email','message')

