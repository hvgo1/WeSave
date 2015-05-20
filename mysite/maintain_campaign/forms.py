from django import forms
from crowdsourcing.models import Campaign, CampaignWish, Wish

class CampaignForm(forms.ModelForm):
    story = forms.CharField(widget=forms.Textarea)
    #wishes = forms.ChoiceField(Wish,through='CampaignWish')
    class Meta:
        model = Campaign
        #fields = ('title', 'beneficiary_name', 'story', 'deadline', 'campaign_image', 'wishes', 'keywords')
        fields = ('title', 'beneficiary_name', 'story', 'deadline', 'campaign_image')

class WishForm(forms.ModelForm):
	class Meta:
		model = Wish
		fields = ('name', 'wish_type')