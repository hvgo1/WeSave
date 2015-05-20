from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from crowdsourcing.models import Campaign, CampaignWish, Wish
from maintain_campaign.forms import CampaignForm, WishForm

def index(request):
    return HttpResponse("You are in campaign index")

def addCampaign(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        campaign_form = CampaignForm(request.POST, request.FILES)

        if campaign_form.is_valid():
            campaign = campaign_form.save(commit=False)
            campaign.created_by = user
            # TODO: set amount to every wish

            campaign.save()
            return index(request)
        else:
            print campaign_form.errors
    else:
        form = CampaignForm()
        form = WishForm()

    return render(request, 'maintain_campaign/add_campaign.html', {'form': campaign_form})

def viewCampaign(request, campaign_title_slug):
    context_dict = {}

    try:
        campaign = Campaign.objects.get(slug=campaign_title_slug)
        wishes = CampaignWish.objects.filter(campaign=campaign)

        context_dict['wishes'] = wishes
        context_dict['campaign'] = campaign
        context_dict['campaign_title_slug'] = campaign.slug

    except Campaign.DoesNotExist:
        # TODO campaign does not exist page
        pass

    return render(request, 'maintain_campaign/view_campaign.html', context_dict)

# TODO: restrict updating of campaign to social worker/wesave admin
def updateCampaign(request, id):
    campaign = Campaign.objects.get(id=id)
    wishes = Wish.objects.all()

    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign.title = request.POST["title"]
            campaign.beneficiary_name = request.POST["beneficiary_name"]
            campaign.story = request.POST["story"]
            campaign.deadline = request.POST["deadline"]
            campaign.campaign_image = request.POST["campaign_image"]
            campaign.save()
            # TODO: update wishes
            #wish = CampaignWish(wish_id=request.POST["wishes"], campaign_id=campaign.id, completed=False, estimated_price=0)
            #wish.save()

            wish = request.POST.get('dropdown_wishes')
            return index(request)
    else:
        form = CampaignForm(instance=campaign)

    return render(request, 'maintain_campaign/update_campaign.html', {'form':form, 'campaign':campaign, 'wishes':wishes})

def donateToCampaign(request):
    #TODO: create donate to campaign page
    #if donation is successful, redirect to save viewCampaign and update campaign status 
    #if donation is cancelled, redirect to delete donation info
    return render(request, 'maintain_campaign/view_campaign.html', context_dict)
