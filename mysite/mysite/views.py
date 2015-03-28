from django.shortcuts import render
from registration.forms import RegistrationForm


class RegistrationFormNoFreeEmail(RegistrationForm):
     
    bad_domains = ['aim.com', 'aol.com', 'email.com','hushmail.com',
                   'mail.ru', 'mailinator.com', 'live.com']


# Create your views here.
def home(request):
    return render(request,'mysite/index.html')

