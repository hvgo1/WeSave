from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from crowdsourcing.models import Campaign, CampaignWish, Wish, UserRole
from maintain_campaign.forms import CampaignForm

def index(request):
    return HttpResponseRedirect('/campaign/list/')

#TODO restrict to social worker/wsadmin
def addCampaign(request, username):
    user = User.objects.get(username=username)
    wishes = Wish.objects.all()
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = user
            # TODO: set amount to every wish

            wish_cost = zip(request.POST.getlist('wishes'), request.POST.getlist('cost'))
            
            if request.POST['submitbutton'] == 'Save':
                campaign.status = 'D'
            elif request.POST['submitbutton'] == 'Submit':
                campaign.status = 'F'

            campaign.save()
            for data in wish_cost:
                wish = Wish.objects.get(name=data[0])
                if wish.id > 1:
                    # TODO: should not submit campaign without wishes
                    if float(data[1]) > float(0):
                        try:
                            CampaignWish.objects.get_or_create(
                                campaign_id = campaign.id,
                                wish_id = wish.id,
                                completed = False,
                                estimated_price = data[1])[0]
                        except:
                            pass

            redirect_link = '/campaign/view/' + campaign.slug + '/'
            return HttpResponseRedirect(redirect_link)
        else:
            print form.errors
    else:
        if request.user.is_authenticated():
            try:
                user_role = UserRole.objects.get(user=user)
            except UserRole.DoesNotExist:
                raise Http404("User role does not exist.")
            if user_role.role == "Soc" or user_role.role == "Adm":
                form = CampaignForm()
            else:
                raise PermissionDenied()
        else:
            return redirect('/login/')

    return render(request, 'maintain_campaign/add_campaign.html', {'form': form, 'wishes':wishes,})

def viewCampaign(request, campaign_title_slug):
    context_dict = {}

    try:
        campaign = Campaign.objects.get(slug=campaign_title_slug)
        wishes = CampaignWish.objects.filter(campaign=campaign)
        if request.user.is_authenticated():
            user_role = UserRole.objects.get(user=request.user)
            context_dict['role'] = user_role.role

        context_dict['wishes'] = wishes
        context_dict['campaign'] = campaign
        context_dict['campaign_title_slug'] = campaign.slug

    except Campaign.DoesNotExist:
        raise Http404("Campaign Page does not exist.")

    return render(request, 'maintain_campaign/view_campaign.html', context_dict)

# TODO: restrict updating of campaign to social worker/wesave admin
def updateCampaign(request, id):
    campaign = Campaign.objects.get(id=id)
    wishes = Wish.objects.all()

    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign.title = request.POST["title"]
            campaign.beneficiary_name = request.POST["beneficiary_name"]
            campaign.story = request.POST["story"]
            campaign.deadline = request.POST["deadline"]
            # TODO: on updating image, delete the previous image, retain previous
            campaign.campaign_image = request.FILES.get('campaign_image', campaign.campaign_image)
            campaign.save()
            # TODO: update wishes
            #wish = CampaignWish(wish_id=request.POST["wishes"], campaign_id=campaign.id, completed=False, estimated_price=0)
            #wish.save()
            #wish = request.POST.get('dropdown_wishes')
            wish_cost = zip(request.POST.getlist('wishes'), request.POST.getlist('cost'))
            
            campaign.save()
            for data in wish_cost:
                wish = Wish.objects.get(name=data[0])
                if wish.id > 1:
                    # TODO: should not submit campaign without wishes
                    if float(data[1]) > float(0):
                        try:
                            CampaignWish.objects.get_or_create(
                                campaign_id = campaign.id,
                                wish_id = wish.id,
                                completed = False,
                                estimated_price = data[1])[0]
                        except:
                            pass
            redirect_link = '/campaign/view/' + campaign.slug + '/'
            return HttpResponseRedirect(redirect_link)
    else:
        if request.user.is_authenticated():
            try:
                user_role = UserRole.objects.get(user=request.user)
            except UserRole.DoesNotExist:
                raise Http404("User role does not exist.")
            if user_role.role == "Soc" or user_role.role == "Adm":
                form = CampaignForm(instance=campaign)
                campaign_wishes = CampaignWish.objects.filter(campaign=campaign.id)
                print campaign_wishes
            else:
                raise PermissionDenied()
        else:
            return redirect('/login/')
        

    return render(request, 'maintain_campaign/update_campaign.html', {'form':form, 'campaign':campaign, 'wishes':wishes, 'campaign_wishes':campaign_wishes})

def donateToCampaign(request):
    #TODO: create donate to campaign page
    #if donation is successful, redirect to save viewCampaign and update campaign status 
    #if donation is cancelled, redirect to delete donation info
    return render(request, 'maintain_campaign/view_campaign.html', context_dict)

def listCampaign(request):
    context_dict = {}
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.get_username())
        context_dict['user'] = user

    campaign_list = Campaign.objects.filter(Q(status="A") | Q(status="C"))
    paginator = Paginator(campaign_list,20) #pagination
    page = request.GET.get('page')
    try:
        campaigns = paginator.page(page) 
    except PageNotAnInteger:
        campaigns = paginator.page(1)
    except EmptyPage:
        campaigns = paginator.page(paginator.num_pages)
    context_dict['campaigns'] = campaigns

    return render_to_response('maintain_campaign/view_campaign_list.html',context_dict)

def viewCampaignDetails(request):
    is_admin = False
    if request.user.is_authenticated():
        try:
            username = request.user.get_username()
            user_object = User.objects.get(username=username)
            user_role = UserRole.objects.get(user=user_object)
        except UserRole.DoesNotExist:
            raise Http404("User role does not exist.")
        if user_role.role == "Adm":
            is_admin = True
            
    campaigns = Campaign.objects.all()
    paginator = Paginator(campaigns,20) #pagination
    page = request.GET.get('page')
    try:
        campaigns = paginator.page(page) 
    except PageNotAnInteger:
        campaigns = paginator.page(1)
    except EmptyPage:
        campaigns = paginator.page(paginator.num_pages)
    return render(request, 'maintain_campaign/view_campaign_details.html',{'campaigns':campaigns,'is_admin':is_admin})
