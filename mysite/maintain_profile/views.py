from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
#from maintain_profile.forms import 
from crowdsourcing.models import UserProfile,Individual,Group, Address

# View
def viewProfile(request,username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user.id)
    
    if Individual.objects.filter(user=user.id).exists():
        details = Individual.objects.get(user=user.id)
        address = Address.objects.get(id=details.id)
        is_indiv = True
    else:
        details = Group.objects.get(user=user.id)
        address = Address.objects.get(id=details.id)
        is_indiv = False
    return render(request,'maintain_profile/viewprofile.html',{'user':user,'profile':profile,'details':details,'address':address,'is_indiv':is_indiv})


