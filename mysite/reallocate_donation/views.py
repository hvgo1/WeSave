from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from crowdsourcing.models import Campaign, CampaignWish

# Shows all wishes and reallocate.
def reallocate(request,id):
    #approved = 'A'
    draft = 'D'
    for_approval = 'F'
    inactive = 'I'

    campaign = Campaign.objects.get(id=id)
    campaigns = Campaign.objects.exclude(Q(status=draft) | Q(status=for_approval) | Q(status=inactive))
    campaigns = campaigns.exclude(id=campaign.id,).order_by('-deadline')#returns all campaigns that the donation can be reallocated
    wishes = CampaignWish.objects.filter(campaign_id=campaign.id) #returns all wishes of the campaign

    if request.method == 'POST':
        to = request.POST.get('campaign')
        wish_id = request.POST['wish_id']
        
        campaign_wish_obj = CampaignWish.objects.get(id=wish_id)
        campaign_wish_obj.campaign_id = to
        campaign_wish_obj.save()


        return HttpResponseRedirect('/wsadmin/campaign/view-details/reallocate/' + unicode(campaign.id) + '/')

    return render(request,'reallocate_donation/reallocate.html', {'wishes': wishes,'campaigns':campaigns})