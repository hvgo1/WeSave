from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from crowdsourcing.models import Campaign
from maintain_campaign.forms import CampaignForm

def index(request):
    return HttpResponse("You are in campaign index")

def add_campaign(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)

        if form.is_valid():
            #campaign = Campaign.objects.get_or_create(
            #    title=request.POST['title'],
            #    beneficiary=request.POST['beneficiary_name'],
            #    story=request.POST['story'],
            #    deadline=request.POST['deadline'],
            #    campaign_image=request.FILES.get['campaign_image','profile_images/def.jpg'],
            #    wishes=request.POST['wishes'],
            #    keywords=request.POST['keywords'],
            #    created_by=1)[0]
            campaign = form.save(commit=False)
            campaign.created_by = user
            campaign.save()
            return index(request)
        else:
            print form.errors
    else:
        form = CampaignForm()

    return render(request, 'maintain_campaign/add_campaign.html', {'form': form})

def view_campaign(request):
    return render(request, 'maintain_campaign/view_campaign.html')