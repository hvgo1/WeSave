from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from registration.forms import RegistrationFormNoFreeEmail
from django.contrib.auth.models import User
from crowdsourcing.forms import UserProfileForm, IndividualForm,GroupForm
from crowdsourcing.models import UserProfile,Individual,Group, UserRole

#Override RegistrationFormNoFreeEmail of Registration package
class RegFormEmail(RegistrationFormNoFreeEmail):
     
    bad_domains = ['aim.com', 'aol.com', 'email.com','hushmail.com',
                   'mail.ru', 'mailinator.com', 'live.com']


# Homepage
def home(request):
    context_dict = {}
    if request.user.is_authenticated():
        try:
            user_role = UserRole.objects.get(user=request.user)
            context_dict['user_role'] = user_role
        except UserRole.DoesNotExist:
            raise Http404("User role does not exist.")
    return render(request,'mysite/index.html', context_dict)

#Individual Registration
def register_individual(request,username):
    user_object = User.objects.get(username=username)
    if request.method == 'GET':
        user_profile_form = UserProfileForm()
        individual_form = IndividualForm()

    else:
        user_profile_form = UserProfileForm(request.POST, request.FILES)
        individual_form = IndividualForm(request.POST)
       
        if user_profile_form.is_valid():
   
            user_profile_object = user_profile_form.save(commit = False) 
            user_profile_object.user_id = user_object.id
            user_profile_object.photo=request.FILES.get('photo','profile_images/def.jpg')
                 
            if individual_form.is_valid():
                individual_object = individual_form.save(commit=False)
                individual_object.user_id=user_object.id  
                individual_object.save()
                role_object=UserRole.objects.get_or_create(role='Don',user_id=user_object.id)[0]
                individual_object.save() 
                user_profile_object.save()          
                return HttpResponseRedirect('/profile/'+username+'/')
    return render(request,'registration/addindividual.html', {'user_profile_form': user_profile_form,'individual_form': individual_form})

#Group Registration
def register_group(request,username):
    user_object = User.objects.get(username=username)
    if request.method == 'GET':
        user_profile_form = UserProfileForm()
        group_form = GroupForm()
 
    else:
        user_profile_form = UserProfileForm(request.POST, request.FILES)
        group_form = GroupForm(request.POST)
   
        if user_profile_form.is_valid():
  
            user_profile_object = user_profile_form.save(commit = False) 
            user_profile_object.user_id = user_object.id
            user_profile_object.photo=request.FILES.get('photo','profile_images/def.jpg')
                         

            if group_form.is_valid():
                group_object = group_form.save(commit=False)
                group_object.user_id=user_object.id    
                role_object=UserRole.objects.get_or_create(role='Don',user_id=user_object.id)[0]    
                group_object.save()
                group_form.save_m2m()   
                user_profile_object.save()          
                return HttpResponseRedirect('/profile/'+username+'/')
    return render(request, 'registration/addgroup.html', {'user_profile_form':user_profile_form, 'group_form':group_form})

#User Authentication
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'mysite/login.html', {'user': user})
            #return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'mysite/login.html', {})

#Restrict
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')
