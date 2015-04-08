from django import forms
from crowdsourcing.models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('title', 'beneficiary_name', 'story', 'deadline', 'campaign_image', 'wishes', 'keywords')
