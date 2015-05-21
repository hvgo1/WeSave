from django import forms
from crowdsourcing.models import Campaign, CampaignWish, Wish

class CampaignForm(forms.ModelForm):
    story = forms.CharField(widget=forms.Textarea)
    #wishes = forms.ChoiceField(Wish,through='CampaignWish')
    class Meta:
        model = Campaign
        #fields = ('title', 'beneficiary_name', 'story', 'deadline', 'campaign_image', 'wishes', 'keywords')
        fields = ('title', 'beneficiary_name', 'story', 'deadline', 'campaign_image',)
        widgets = {
            'deadline': forms.DateInput(attrs={'class':'datepicker'})
        }

class WishForm(forms.ModelForm):
	#wish = forms.ChoiceField(Wish)
	class Meta:
		model = Wish
		fields = ('name',)

