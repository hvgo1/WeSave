from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger
from crowdsourcing.models import Campaign

#Approve all checked Campaigns
def approve(request):

    if request.method == 'POST':
        checked_campaigns = request.POST.getlist('checks')
        for checked in checked_campaigns:
            campaign = Campaign.objects.get(id=checked)
            campaign.status = 'A'
            campaign.save()
            print campaign.status
    return forapproval_campaigns(request)


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
    return render(request,'verify_campaign/view_campaign_list.html',{'campaigns':campaigns})