from django.shortcuts import render
from django.shortcuts import redirect,render_to_response
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger
from crowdsourcing.models import UserProfile, Individual, UserRole
from django.contrib.auth.models import User


#Edit UserRole of User to Social Worker or WSAdmin
def add_role(request):

    if request.method == 'POST':
        checked_individuals = request.POST.getlist('checks')
        choice_role = request.POST.get('role')

        if choice_role == 'social_worker':
            role = 'Soc'
        else:
            role = 'Adm'

        for checked in checked_individuals:

            user_object = UserRole.objects.get(user_id=checked)
            user_object.role = role
            user_object.save()
    

    return users_list(request)


#Lists all users 
def users_list(request): 
    #roles = UserRole.objects.filter(user=user) #returns all campaigns where the user is a donor
    
    if request.user.is_authenticated():
        try:
            username = request.user.get_username()
            user_object = User.objects.get(username=username)
            user_role = UserRole.objects.get(user=user_object)
        except UserRole.DoesNotExist:
            raise Http404("User role does not exist.")
        if user_role.role == "Adm":
            individual_list = Individual.objects.order_by('user_id')#user.username
            userrole_list = UserRole.objects.order_by('user_id')
            paginator = Paginator(individual_list,8) #pagination
            page = request.GET.get('page')
            try:
                individuals = paginator.page(page) 
            except PageNotAnInteger:
                individuals = paginator.page(1)
            except EmptyPage:
                individuals = paginator.page(paginator.num_pages)
            return render(request,'manage_social_workers/view_individuals_list.html',{'individuals':individuals,'userrole_list':userrole_list})
        else:        
            raise PermissionDenied()
    else:
        return redirect('/login/')
    