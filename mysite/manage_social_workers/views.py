from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger
from crowdsourcing.models import UserProfile, Individual, UserRole
from django.contrib.auth.models import User


#Edit UserRole of User to Social Worker or WSAdmin
#def add(request):

#    if request.method == 'POST':
#        checked_campaigns = request.POST.getlist('checks')
#        for checked in checked_campaigns:
#            campaign = Campaign.objects.get(id=checked)
 #           campaign.status = 'A'
 #           campaign.save()
 #           print campaign.status
 #   return forapproval_campaigns(request)


#Lists all campaigns for approval/verification
def users_list(request): 
  
    individual_list = Individual.objects.order_by('user')#user.username
    paginator = Paginator(individual_list,8) #pagination
    page = request.GET.get('page')
    try:
    	individuals = paginator.page(page) 
    except PageNotAnInteger:
        individuals = paginator.page(1)
    except EmptyPage:
        individuals = paginator.page(paginator.num_pages)
    return render(request,'manage_social_workers/view_individuals_list.html',{'individuals':individuals})