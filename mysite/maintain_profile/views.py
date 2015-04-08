from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
#from maintain_profile.forms import 
from crowdsourcing.models import UserProfile,Individual,Group, Address,Campaign_User_Donor,Campaign_User_Followers,Campaign

# View
def viewProfile(request,username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user.id)
    donor = Campaign_User_Donor.objects.filter(user=user)
    sub = Campaign_User_Followers.objects.filter(user=user)
    created = Campaign.objects.filter(created_by_id=user.id)
    
    if Individual.objects.filter(user=user.id).exists():
        details = Individual.objects.get(user=user.id)
        address = Address.objects.get(id=details.id)
        is_indiv = True
    else:
        details = Group.objects.get(user=user.id)
        address = Address.objects.get(id=details.id)
        is_indiv = False
    return render(request,'maintain_profile/viewprofile.html',{'user':user,'created':created,'sub':sub,'donor':donor,'profile':profile,'details':details,'address':address,'is_indiv':is_indiv})

#LIST
def listProfile(request):
    userlist = UserProfile.objects.order_by('user')
    paginator = Paginator(userlist,8)
    page = request.GET.get('page')
    try:
    	users = paginator.page(page) 
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render_to_response('maintain_profile/viewprofilelist.html',{'users':users})