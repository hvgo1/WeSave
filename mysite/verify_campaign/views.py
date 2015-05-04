from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger
from crowdsourcing.models import Campaign

def approve(request):
    print "hi"
    if request.method == 'post':
        checked_campaigns = request.POST.getlist('checks')
        print checked_campaigns
        for checked in checked_campaigns:
            print checked
            campaign = Campaign.objects.get(id=checked)
            print campaign.status	
            campaign.status = 'V'
    return forapproval_campaigns(request)
# Create your views here.

#Lists all campaigns for approval/verification
def forapproval_campaigns(request): 
    campaign_list = Campaign.objects.order_by('id').filter(status='F')
    paginator = Paginator(campaign_list,8) #pagination
    page = request.GET.get('page')
    try:
    	campaigns = paginator.page(page) 
    except PageNotAnInteger:
        campaigns = paginator.page(1)
    except EmptyPage:
        campaigns = paginator.page(paginator.num_pages)
    return render_to_response('verify_campaign/view_campaign_list.html',{'campaigns':campaigns})