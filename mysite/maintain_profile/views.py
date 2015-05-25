from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
#from maintain_profile.forms import 
from crowdsourcing.models import UserProfile,Individual,Group,CampaignUserDonor,CampaignUserFollowers,Campaign
from crowdsourcing.forms import UserProfileForm, IndividualForm,GroupForm

#View individual profile of users [privacy options pa]
def view_profile(request,username): 
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user_id=user.id) 
    donor = CampaignUserDonor.objects.filter(user_id=user) #returns all campaigns where the user is a donor
    sub = CampaignUserFollowers.objects.filter(user_id=user) #returns all campaigns where the user is a subscriber/follower
    created = Campaign.objects.filter(created_by_id=user.id) #returns all campaigns where the user is a creator [by social workers only]
    
    if Individual.objects.filter(user_id=user.id).exists():
        details = Individual.objects.get(user_id=user.id)
        is_indiv = True
    else:
        details = Group.objects.get(user_id=user.id)
        is_indiv = False
    return render(request,'maintain_profile/viewprofile.html',{'user':user,'created':created,'sub':sub,'donor':donor,'profile':profile,'details':details,'is_indiv':is_indiv})

def update_profile(request,username): 
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user_id=user.id) 
    if Individual.objects.filter(user_id=user.id).exists():
        individual_details = Individual.objects.get(user_id=user.id)
        if request.method == 'GET':
            user_profile_form = UserProfileForm(instance=profile)
            individual_form = IndividualForm(instance=individual_details)
        else:
            user_profile_form = UserProfileForm(request.POST, request.FILES,instance=profile)
            individual_form = IndividualForm(request.POST,instance=individual_details)  
        if user_profile_form.is_valid(): 
            profile.photo=request.FILES.get('photo','profile_images/def.jpg')
            profile.save() 
            if individual_form.is_valid():
                individual_details.save()                          
                return HttpResponseRedirect('/profile/'+username+'/')
        return render(request,'maintain_profile/updateprofile.html', {'user_profile_form': user_profile_form,'individual_form': individual_form,'action':'update/'+ username})

    elif Group.objects.filter(user_id=user.id).exists():
        group_details = Group.objects.get(user_id=user.id)
        if request.method == 'GET':
            user_profile_form = UserProfileForm(instance=profile)
            group_form = GroupForm(instance=group_details)
        else:
            user_profile_form = UserProfileForm(request.POST, request.FILES,instance=profile)
            group_form = GroupForm(request.POST,instance=group_details)  
        if user_profile_form.is_valid(): 
            profile.photo=request.FILES.get('photo','profile_images/def.jpg')
            profile.save() 
            if group_form.is_valid():
                #group_details.document=request.FILES.get('document', None) 
                #group_details.page_address=request.POST.get('page_address',None)
                #group_details.registration_number=request.POST.get('registration_number',None)
                #group_details.comments=request.POST.get('comments',None),
                group_details.name=request.POST['name']
                group_details.page_address=request.POST.get('page_address',None) #or ""Blank
                group_details.about=request.POST['about']
                group_details.service_category=request.POST['service_category']
                group_details.registration_number=int(request.POST.get('registration_number',None))
                group_details.document=request.FILES.get('document', None)
                group_details.comments=request.POST.get('comments',None)
                group_details.pc_first_name = request.POST['pc_first_name']
                group_details.pc_last_name = request.POST['pc_last_name']
                group_details.pc_email = request.POST['pc_email']
                group_details.pc_job_title = request.POST['pc_job_title']
                group_details.pc_phone_number = request.POST['pc_phone_number']
                group_details.sc_first_name = request.POST['sc_first_name']
                group_details.sc_last_name = request.POST['sc_last_name']
                group_details.sc_email = request.POST['sc_email']
                group_details.sc_job_title = request.POST['sc_job_title']
                group_details.sc_phone_number = request.POST['sc_phone_number']
                group_details.user_id=user.id
                group_details.save()            
            return HttpResponseRedirect('/profile/'+username+'/')
    return render(request, 'maintain_profile/updateprofile.html', {'user_profile_form':user_profile_form, 'group_form':group_form})
   

#Lists all user profiles
def list_profile(request): 
    userlist = UserProfile.objects.order_by('user')
    paginator = Paginator(userlist,8) #pagination
    page = request.GET.get('page')
    try:
    	users = paginator.page(page) 
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render_to_response('maintain_profile/viewprofilelist.html',{'users':users})
#copy to campaign module
def campaign(request):
    return render(request,'mysite/campaign.html')
