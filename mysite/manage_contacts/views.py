from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from crowdsourcing.models import Contact
# Create your views here.

def contactus(request):
   if request.method == 'POST':

       name = request.POST.get('name')
       email = request.POST.get('email')
       message = request.POST.get('message')


       msg = Contact.objects.get_or_create(name=name, 
              email=email,message=message)[0]            
       msg.save() 
   else: 
       return HttpResponseRedirect('/home/#contact')           
   return HttpResponseRedirect('/home/')
