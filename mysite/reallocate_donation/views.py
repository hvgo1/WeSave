from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from crowdsourcing.models import Campaign, CampaignWish

# Shows all wishes and reallocate.
def reallocate(request,id):
    approved = 'A'
    campaign = Campaign.objects.get(id=id)
    campaigns = Campaign.objects.filter(status=approved).order_by('-deadline')
    wishes = CampaignWish.objects.filter(campaign_id=campaign.id) #returns all wishes of the campaign

    if request.method == 'POST':
        to = request.POST['value']
        wish_id = request.POST['wish_id']
        
        campaign_wish_obj = CampaignWish.objects.get(id=wish_id)
        campaign_wish_obj.campaign_id = to
        campaign.save()

    return render(request,'reallocate_donation/reallocate.html', {'wishes': wishes,'campaigns':campaigns})