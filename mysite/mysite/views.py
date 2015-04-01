from django.shortcuts import render
from registration.forms import RegistrationFormNoFreeEmail


class RegFormEmail(RegistrationFormNoFreeEmail):
     
    bad_domains = ['aim.com', 'aol.com', 'email.com','hushmail.com',
                   'mail.ru', 'mailinator.com', 'live.com']


# Create your views here.
def home(request):
    return render(request,'mysite/index.html')

def register_continue(request):
    return render(request,'registration/registration_continue.html')

