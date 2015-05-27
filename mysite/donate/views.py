from django.shortcuts import render,HttpResponseRedirect
from donate.forms import InkindForm1,InkindForm2,InkindForm3
from django.contrib.auth.models import User
from crowdsourcing.models import Campaign,Individual,Group, UserProfile, UnregisteredDonor

def donate_inkind(request,campaign_title_slug):
    campaign = Campaign.objects.get(slug=campaign_title_slug)
    if request.method == 'GET':
        
        if request.user.is_authenticated():
            username = request.user.get_username()
            user_object = User.objects.get(username=username)
            if Individual.objects.filter(user_id=user_object.id).exists():
                    is_individual = True
                    inkind_form = InkindForm2()
            else:
                    is_individual = False
                    inkind_form = InkindForm3()
            is_logged_in = True
            if is_logged_in == True:
                    print "true"
            #username = request.user.get_username()
            
        else:
            is_individual = False
            inkind_form = InkindForm1()
            is_logged_in = False
            if is_logged_in == False:
                    print "F"
        
    else:

        print "post"
 
        if request.user.is_authenticated():
            is_logged_in = True
            if is_logged_in == True:
                print "true" 
            username = request.user.get_username()
            user_object = User.objects.get(username=username)
            print user_object.username
            profile = UserProfile.objects.get(user_id=user_object.id)
   
            if Individual.objects.filter(user_id=user_object.id).exists():
                print "indiv" 
                is_individual = True
                inkind_form = InkindForm2(request.POST)
                
                if inkind_form.is_valid():
                    inkind_object = inkind_form.save(commit=False)
                    
                    inkind_object.pc_contact_number = member.phone_number
                    inkind_object.name = user_object.username
                    inkind_object.email = user_object.email
                    inkind_object.address = profile.street + "," + profile.barangay+ "," + profile.city + "," + profile.country
                    inkind_object.campaign_id = campaign.id
                    inkind_object.save() 
                    print is_logged_in
            else:
                print "group" 
                is_individual = False
                inkind_form = InkindForm3(request.POST)
                
                if inkind_form.is_valid():
                    inkind_object = inkind_form.save(commit=False)
                    
                    inkind_object.pc_contact_number = member.pc_contact_number
                    inkind_object.sc_contact_number = member.sc_contact_number
                    inkind_object.name = user_object.username
                    inkind_object.email = user_object.email
                    inkind_object.address = profile.street + "," + profile.barangay+ "," + profile.city + "," + profile.country
                    inkind_object.campaign_id = campaign.id
                    inkind_object.save() 
                    print is_logged_in

            
        else:
            is_individual = False
            is_logged_in = False
            inkind_form = InkindForm1(request.POST)
            
            if inkind_form.is_valid():
                inkind_object = inkind_form.save(commit=False)
                if is_logged_in == False:
                    print "F"
                unregistered_donor = UnregisteredDonor.objects.get_or_create(name=request.POST['name'],
                                     campaign_id=campaign.id,
                                     amount=request.POST['fair_market_value'])[0]
                inkind_object.campaign_id = campaign.id
                inkind_object.save()          
        return HttpResponseRedirect('/home/')
    return render(request,'donate/inkind.html',{'inkind_form':inkind_form,'is_logged_in':is_logged_in,'is_individual':is_individual})