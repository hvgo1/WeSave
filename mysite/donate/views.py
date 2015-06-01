from django.shortcuts import render,HttpResponseRedirect
from donate.forms import InkindForm1,InkindForm2,InkindForm3
from django.contrib.auth.models import User
from crowdsourcing.models import Campaign,Individual,Group, UserProfile, UnregisteredDonor


def donate_inkind(request,campaign_title_slug):
    campaign = Campaign.objects.get(slug=campaign_title_slug)
    username = ""
    if request.method == 'GET':
        
        if request.user.is_authenticated():
            logged_in = True
            username = request.user.get_username()
            user_object = User.objects.get(username=username)
            if Individual.objects.filter(user_id=user_object.id).exists():
 
                    inkind_form = InkindForm2()
            elif Group.objects.filter(user_id=user_object.id).exists():

                    inkind_form = InkindForm3()
  
        else:
            logged_in = False
            inkind_form = InkindForm1()
   
    else:

        if request.user.is_authenticated():
            logged_in = True
            username = request.user.get_username()
            user_object = User.objects.get(username=username)
         
            profile = UserProfile.objects.get(user_id=user_object.id)
   
            if Individual.objects.filter(user_id=user_object.id).exists():
      
                inkind_form = InkindForm2(request.POST)
                
                if inkind_form.is_valid():
                   
                    inkind_object = inkind_form.save(commit=False)
                    member = Individual.objects.get(user_id=user_object.id)
                    inkind_object.pc_contact_number = member.phone_number
                    inkind_object.name = user_object.username
                    inkind_object.email = user_object.email
                    if profile.barangay == None :
                        barangay = " "

                    else:
                        barangay = profile.barangay
                    if profile.city == None :
                        city = " "
                    else:
                        city = profile.city              

                    inkind_object.address = profile.street +  unicode(barangay) + unicode(city) + unicode(profile.country.name)
                    inkind_object.campaign_id = campaign.id
                    inkind_object.save() 
           
            else:
              
                inkind_form = InkindForm3(request.POST)
                
                if inkind_form.is_valid():
                    inkind_object = inkind_form.save(commit=False)
                    member = Group.objects.get(user_id=user_object.id)
                    inkind_object.pc_contact_number = member.pc_phone_number
                    inkind_object.sc_contact_number = member.sc_phone_number
                    inkind_object.name = user_object.username
                    inkind_object.email = user_object.email
                    if profile.barangay == None :
                        barangay = " "

                    else:
                        barangay = profile.barangay
                    if profile.city == None :
                        city = " "
                    else:
                        city = profile.city    
                    inkind_object.address = profile.street +  unicode(barangay) + unicode(city) + unicode(profile.country.name)
                    inkind_object.campaign_id = campaign.id
                    inkind_object.save() 
                  

            
        else:
            logged_in = False
            inkind_form = InkindForm1(request.POST)
            
            if inkind_form.is_valid():
                inkind_object = inkind_form.save(commit=False)
                
                unregistered_donor = UnregisteredDonor.objects.get_or_create(name=request.POST['name'],
                                     campaign_id=campaign.id,
                                     amount=request.POST['fair_market_value'])[0]
                inkind_object.campaign_id = campaign.id
                inkind_object.save()          
        return HttpResponseRedirect('/home/')
    return render(request,'donate/inkind.html',{'inkind_form':inkind_form, 'campaign':campaign,'logged_in':logged_in,'username':username})

def donate_monetary(request, campaign_title_slug):
    context_dict = {}
    campaign = Campaign.objects.get(slug=campaign_title_slug)
    context_dict['campaign'] = campaign

    if request.method == 'POST':
        print 'POST'
    else:
        print 'GET'

    return render(request, 'donate/monetary.html', context_dict)

def success(request, campaign_title_slug):
    #TODO: update campaign status and donor list

    redirect_link = '/campaign/view/' + campaign_title_slug + '/'
    return HttpResponseRedirect(redirect_link)

def cancelled(request, campaign_title_slug):
    redirect_link = '/donate/monetary/' + campaign_title_slug + '/'
    return HttpResponseRedirect(redirect_link)
