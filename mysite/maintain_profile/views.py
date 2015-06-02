from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render, render_to_response, redirect
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from crowdsourcing.models import UserProfile,UserRole,Individual,Group,CampaignUserDonor,CampaignUserFollowers,Campaign
from crowdsourcing.forms import UserProfileForm, IndividualForm,GroupForm


def restrictView(request,profile_owner,action):
    VIEW = 1
    UPDATE = 2
    LIST = 3
    if request.user.is_authenticated():
        try:
            username = request.user.get_username()
            user_object = User.objects.get(username=username)
            user_role = UserRole.objects.get(user=user_object)
        except UserRole.DoesNotExist:
            raise Http404("User role does not exist.")
        if action == VIEW:
            if user_role.role == "Adm" or username == profile_owner:
                return True
            else:        
                raise PermissionDenied()
        if action == UPDATE:
            if username == profile_owner:
                return True
            else:        
                raise PermissionDenied()
        if action == LIST:
            if user_role.role == "Adm":
                return True
            else:        
                raise PermissionDenied()        
    else:
        return False
   
#View individual profile of users [privacy options pa]
def viewProfile(request,username): 
    action = 1
    allow_view = restrictView(request,username,action)
    if allow_view == True:
        user_object = User.objects.get(username=username)
        profile = UserProfile.objects.get(user_id=user_object.id) 
        donor = CampaignUserDonor.objects.filter(user_id=user_object.id) #returns all campaigns where the user is a donor
        sub = CampaignUserFollowers.objects.filter(user_id=user_object.id) #returns all campaigns where the user is a subscriber/follower
        created = Campaign.objects.filter(created_by_id=user_object.id) #returns all campaigns where the user is a creator [by social workers only]
    
        if Individual.objects.filter(user_id=user_object.id).exists():
            details = Individual.objects.get(user_id=user_object.id)
            is_indiv = True
        else:
            details = Group.objects.get(user_id=user_object.id)
            is_indiv = False
        return render(request,'maintain_profile/viewprofile.html',{'user_object':user_object,'created':created,'sub':sub,'donor':donor,'profile':profile,'details':details,'is_indiv':is_indiv})
    else:
        return redirect('/login/')
#Update profiles of users
def updateProfile(request,username):
    action = 2
    allow_view = restrictView(request,username,action)
    if allow_view == True: 
        user_object = User.objects.get(username=username)
        profile = UserProfile.objects.get(user_id=user_object.id) 
        if Individual.objects.filter(user_id=user_object.id).exists():
            individual_details = Individual.objects.get(user_id=user_object.id)
            if request.method == 'GET':
                user_profile_form = UserProfileForm(instance=profile)
                individual_form = IndividualForm(instance=individual_details)
            else:
                user_profile_form = UserProfileForm(request.POST, request.FILES,instance=profile)
                individual_form = IndividualForm(request.POST,instance=individual_details)  
            if user_profile_form.is_valid(): 
            #profile.photo=request.FILES.get('photo','profile_images/def.jpg')
                if individual_form.is_valid():
                    individual_details.save()  
                    profile.save()                         
                    return HttpResponseRedirect('/profile/'+username+'/')
            return render(request,'maintain_profile/updateprofile.html', {'user_profile_form': user_profile_form,'individual_form': individual_form,'action':'update/'+ username})

        elif Group.objects.filter(user_id=user_object.id).exists():
            group_details = Group.objects.get(user_id=user_object.id)
            if request.method == 'GET':
                user_profile_form = UserProfileForm(instance=profile)
                group_form = GroupForm(instance=group_details)
            else:
                user_profile_form = UserProfileForm(request.POST, request.FILES,instance=profile)
                group_form = GroupForm(request.POST,instance=group_details)  
            if user_profile_form.is_valid(): 
            #profile.photo=request.FILES.get('photo','profile_images/def.jpg')
            
                if group_form.is_valid():
                          
                    for category in group_details.service_category.all():
                        category.delete()
                    categories = group_form.cleaned_data['service_category']
                    for category in categories:
                        group_details.service_category.add(category)

                    group_details.save()   
                    profile.save()          
                return HttpResponseRedirect('/profile/'+username+'/')
        return render(request, 'maintain_profile/updateprofile.html', {'user_profile_form':user_profile_form, 'group_form':group_form})
   
    else:
        return redirect('/login/')


#Lists all user profiles [for future use]
def listProfile(request): 
    action = 3
    username = None

    context_dict = {}
    if request.user.is_authenticated():
        user = request.user
        context_dict['user'] = user

    allow_view = restrictView(request,username,action)
    if allow_view == True:
        userlist = UserProfile.objects.order_by('user_id')
        paginator = Paginator(userlist,8) #pagination
        page = request.GET.get('page')
        try:
    	    users = paginator.page(page) 
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        context_dict['users'] = users
        return render_to_response('maintain_profile/viewprofilelist.html',context_dict)
    else:
        return redirect('/login/')
#copy to campaign module
def campaign(request):
    return render(request,'mysite/campaign.html')
