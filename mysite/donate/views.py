from django.shortcuts import render
from donate.forms import InkindForm
from crowdsourcing.models import Campaign

def donate_inkind(request,campaign_title_slug):
    campaign = Campaign.objects.get(slug=campaign_title_slug)
    if request.method == 'GET':
        inkind_form = InkindForm()
        if request.user.is_authenticated():
            
            is_logged_in = True
            #username = request.user.get_username()
            
        else:
            is_logged_in = False
        
    else:
        inkind_form = InkindForm(request.POST)
        
        if inkind_form.is_valid():
            inkind_object = inkind_form.save(commit=False)
            if request.user.is_authenticated():
            
                username = request.user.get_username()
                user_object = User.objects.get(username=username)
                profile = UserProfile.objects.get(user_id=user_object.id)
   
                if Individual.objects.filter(user_id=user_object.id).exists():
                    member = Individual.objects.get(user_id=user_object.id)
                    inkind_object.pc_contact_number = member.phone_number
                else:
                    member = Group.objects.get(user_id=user_object.id)
                    inkind_object.pc_contact_number = member.pc_contact_number
                    inkind_object.sc_contact_number = member.sc_contact_number
                
                inkind_object.name = user_object.id
                inkind_object.email = user_object.email
                inkind_object.address = profile.street + "," + profile.barangay+ "," + profile.city + "," + profile.country
                inkind_object.campaign = campaign.id
            else:
                unregistered_donor = UnregisteredDonor.objects.get_or_create(name=request.POST['name'],
                                     campaign_id=campaign.id,
                                     amount=request.POST['fair_market_value'])[0]

            inkind_object.save()          
            return HttpResponseRedirect('/home/')
    return render(request,'donate/inkind.html',{'inkind_form':inkind_form,'is_logged_in':is_logged_in})