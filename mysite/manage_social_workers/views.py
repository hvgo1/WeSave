from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger
from crowdsourcing.models import UserProfile, Individual, UserRole
from django.contrib.auth.models import User


#Edit UserRole of User to Social Worker or WSAdmin
def add_role(request):

    if request.method == 'POST':
        checked_individuals = request.POST.getlist('checks')
        choice_role = request.POST.get('role')
        print choice_role
        if choice_role == 'social_worker':
            role = 'Soc'
        else:
            role = 'Adm'
        print checked_individuals
        for checked in checked_individuals:
            print checked
            
            user = UserRole.objects.get_or_create(user_id=checked,role=role)[0]
            #user.role = 'Adm'
 			 #user.role = 'Soc'
            #campaign.save()
            print user.role
    return users_list(request)


#Lists all users 
def users_list(request): 
    #roles = UserRole.objects.filter(user=user) #returns all campaigns where the user is a donor
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