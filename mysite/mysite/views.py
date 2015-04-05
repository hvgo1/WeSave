from django.shortcuts import render
from django.http import HttpResponseRedirect
from registration.forms import RegistrationFormNoFreeEmail
from django.contrib.auth.models import User
from crowdsourcing.forms import UserProfileForm, IndividualForm,GroupForm,AddressForm
from crowdsourcing.models import UserProfile, Address,Individual,Group

class RegFormEmail(RegistrationFormNoFreeEmail):
     
    bad_domains = ['aim.com', 'aol.com', 'email.com','hushmail.com',
                   'mail.ru', 'mailinator.com', 'live.com']


# Create your views here.
def home(request):
    return render(request,'mysite/index.html')

def register_individual(request,username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        userform = UserProfileForm()
        indivform = IndividualForm()
        addform = AddressForm()
    else:
        userform = UserProfileForm(request.POST, request.FILES)
        indivform = IndividualForm(request.POST)
        addform = AddressForm(request.POST)
        if userform.is_valid():
            if addform.is_valid():
                a=addform.save()
                u = UserProfile.objects.get_or_create(photo=request.FILES.get('photo', None), 
                address_id=a.id,user_id=user.id,role=request.POST['role'])[0]            
                u.save()            
            if indivform.is_valid():
                i = Individual.objects.get_or_create(first_name=request.POST['first_name'], 
                middle_name=request.POST.get('middle_name',None), #or ""Blank
                last_name=request.POST['last_name'],birthday=request.POST['birthday'],user_id=user.id)[0]            
                i.save()            
                return HttpResponseRedirect('/home/')
    return render(request,'registration/addindividual.html', {'userform': userform,'indivform': indivform,'addform':addform})

def register_group(request,username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        userform = UserProfileForm()
        groupform = GroupForm()
        addform = AddressForm()
    else:
        userform = UserProfileForm(request.POST, request.FILES)
        groupform = GroupForm(request.POST)
        addform = AddressForm(request.POST)
        if userform.is_valid():
            if addform.is_valid():
                a=addform.save()
                u = UserProfile.objects.get_or_create(photo=request.FILES.get('photo', None), 
                address_id=a.id,user_id=user.id,role=request.POST['role'])[0]            
                u.save()            
            if groupform.is_valid():
                i = Group.objects.get_or_create(name=request.POST['name'], 
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
                i.save()            
                return HttpResponseRedirect('/home/')
    return render(request,'registration/addgroup.html', {'userform': userform,'groupform': groupform,'addform':addform})
