from django.shortcuts import render
from django.http import HttpResponseRedirect
from registration.forms import RegistrationFormNoFreeEmail
from django.contrib.auth.models import User
from crowdsourcing.forms import UserProfileForm, IndividualForm,GroupForm

class RegFormEmail(RegistrationFormNoFreeEmail):
     
    bad_domains = ['aim.com', 'aol.com', 'email.com','hushmail.com',
                   'mail.ru', 'mailinator.com', 'live.com']


# Create your views here.
def home(request):
    return render(request,'mysite/index.html')

def register_individual(request,username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        form = UserProfileForm()
        form1 = IndividualForm()
    else:
        form = UserProfileForm(request.POST, request.FILES,)
        form1 = IndividualForm(request.POST)
        #HIDE USER FIELD, SET USER FIELD TO USER.ID

        #request.POST = request.POST.copy()
        #request.POST['user_id'] = user.id
        #form = UserProfileForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            if form1.is_valid():
                form1.save()
                return HttpResponseRedirect('/home/')
    return render(request,'registration/addindividual.html', {'form': form,'form1': form1})

def register_group(request,username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        form = UserProfileForm()
        form1 = GroupForm()
    else:
        form = UserProfileForm(request.POST, request.FILES,)
        form1 = GroupForm(request.POST)
        #HIDE USER FIELD, SET USER FIELD TO USER.ID
        if form.is_valid():
            form.save()
            if form1.is_valid():
                form1.save()
                return HttpResponseRedirect('/home/')
    return render(request,'registration/addgroup.html', {'form': form,'form1': form1})

