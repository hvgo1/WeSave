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
    return render(request,'mysite/index.html')

#Individual Registration
def register_individual(request,username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        user_profile_form = UserProfileForm()
        individual_form = IndividualForm()

    else:
        user_profile_form = UserProfileForm(request.POST, request.FILES)
        individual_form = IndividualForm(request.POST)
       
        if user_profile_form.is_valid():
   
            user_profile_object = user_profile_form.save(commit = False) 
            user_profile_object.user_id = user.id
            user_profile_object.photo=request.FILES.get('photo','profile_images/def.jpg')
            user_profile_object.save()     

            if individual_form.is_valid():
                
                individual_object = Individual.objects.get_or_create(first_name=request.POST['first_name'], 
                middle_name=request.POST.get('middle_name',None), #or ""Blank
                last_name=request.POST['last_name'],birthday=request.POST['birthday'],user_id=user.id)[0]                            
                role_object=UserRole.objects.get_or_create(role='Don',user_id=user.id)[0]
                role_object.save()
                individual_object.save()            
                return HttpResponseRedirect('/profile/'+username+'/')
    return render(request,'registration/addindividual.html', {'user_profile_form': user_profile_form,'individual_form': individual_form})

#Group Registration
def register_group(request,username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        user_profile_form = UserProfileForm()
        group_form = GroupForm()
 
    else:
        user_profile_form = UserProfileForm(request.POST, request.FILES)
        group_form = GroupForm(request.POST)
   
        if user_profile_form.is_valid():
  
            user_profile_object = user_profile_form.save(commit = False) 
            user_profile_object.user_id = user.id
            user_profile_object.photo=request.FILES.get('photo','profile_images/def.jpg')
            user_profile_object.save()              

            if group_form.is_valid():

                group_object = Group.objects.get_or_create(name=request.POST['name'], 
                page_address=request.POST.get('page_address',None), #or ""Blank
                about=request.POST['about'],
                service_category=request.POST['service_category'],
                registration_number=request.POST.get('registration_number',None),
                document=request.FILES.get('document', None),
                comments=request.POST.get('comments',None),
                pc_first_name = request.POST['pc_first_name'],
                pc_last_name = request.POST['pc_last_name'],
                pc_email = request.POST['pc_email'],
                pc_job_title = request.POST['pc_job_title'],
                pc_phone_number = request.POST['pc_phone_number'],
                sc_first_name = request.POST['sc_first_name'],
                sc_last_name = request.POST['sc_last_name'],
                sc_email = request.POST['sc_email'],
                sc_job_title = request.POST['sc_job_title'],
                sc_phone_number = request.POST['sc_phone_number'],
                user_id=user.id)[0]        
                role_object=UserRole.objects.get_or_create(role='Don',user_id=user.id)[0]    
                group_object.save()            
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
