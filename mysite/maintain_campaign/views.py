from django.http import HttpResponse
from django.shortcuts import render

from crowdsourcing.models import Campaign
from maintain_campaign.forms import CampaignForm

def index(request):
    return HttpResponse("You are in campaign index")
#'title', 'beneficiary_name', 'story', 'deadline', 'campaign_image', 'wishes', 'keywords'
def add_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)

        if form.is_valid():
            campaign = form.save(commit=False)
            #campaign.title = request.POST.get('title')
            return index(request)
        else:
            print form.errors
    else:
        form = CampaignForm()

    return render(request, 'maintain_campaign/add_campaign.html', {'form': form})

