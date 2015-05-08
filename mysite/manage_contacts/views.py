from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from manage_contacts.forms import ContactForm
from crowdsourcing.models import Contact
# Create your views here.

def contact_us(request):

    if request.method == 'GET': 
        contact_form = ContactForm()

    else:
        contact_form = ContactForm(request.POST)
       #name = request.POST.get('name')
       #email = request.POST('email')
       #message = request.POST('message')


       #msg = Contact.objects.get_or_create(name=name, 
        #      email=email,message=message)[0] 
        if contact_form.is_valid():           
            contact_form.save() 
        return HttpResponseRedirect('/contact/')           
    return render(request, 'manage_contacts/contact.html', {'contact_form':contact_form,})
