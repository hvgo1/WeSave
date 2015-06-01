from django.shortcuts import render
from django.shortcuts import redirect,render_to_response
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger
from crowdsourcing.models import Campaign,UserRole
from django.contrib.auth.models import User

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
  
    if request.user.is_authenticated():
        try:
            username = request.user.get_username()
            user_object = User.objects.get(username=username)
            user_role = UserRole.objects.get(user=user_object)
        except UserRole.DoesNotExist:
            raise Http404("User role does not exist.")
        if user_role.role == "Adm":
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

        else:        
            raise PermissionDenied()
    else:
        return redirect('/login/')