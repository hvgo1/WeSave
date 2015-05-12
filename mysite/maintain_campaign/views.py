from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from crowdsourcing.models import Campaign, CampaignWish, Wish
from maintain_campaign.forms import CampaignForm

def index(request):
    return HttpResponse("You are in campaign index")

def addCampaign(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)

        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = user
            campaign.save()
            return index(request)
        else:
            print form.errors
    else:
        form = CampaignForm()

    return render(request, 'maintain_campaign/add_campaign.html', {'form': form})

def viewCampaign(request, campaign_title_slug):
    context_dict = {}

    try:
        campaign = Campaign.objects.get(slug=campaign_title_slug)
        wishes = CampaignWish.objects.filter(campaign=campaign)

        for wish in wishes:
            print Wish.objects.get(id=wish.id).name

        context_dict['wishes'] = wishes
        context_dict['campaign'] = campaign
        context_dict['campaign_title_slug'] = campaign.slug

    except Campaign.DoesNotExist:
        pass

    return render(request, 'maintain_campaign/view_campaign.html', context_dict)