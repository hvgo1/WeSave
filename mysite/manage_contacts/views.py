from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from manage_contacts.forms import ContactForm
from crowdsourcing.models import Contact
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import django
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def contact_us(request):
    import smtplib
    if request.method == 'GET': 
        contact_form = ContactForm()

    else:
        contact_form = ContactForm(request.POST)
  
        if contact_form.is_valid():

#           print "Sending Email"
 #          mail_title = 'Test Email'
  #         message = 'This is a test email.' 
   #        email = settings.DEFAULT_FROM_EMAIL
    #       recipients = [settings.DEFAULT_TO_EMAIL]
     #      send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,['j25_jessie@yahoo.com'], fail_silently=False)
           #send_mail(mail_title, message, email, recipients, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD) 
      #     print "Email Sent"
            #name = request.POST.get('name','')
            #email = request.POST.get('email','')
            #message = request.POST.get('message','')   
            #subject = 'Message from %s ' %name
            #if subject and message and email: 
             #   try:
                    #send_mail(subject, message, email, ['jessica.pabico@gmail.com'])
                    #email = EmailMessage(subject, message, to=['j25_jessie@yahoo.com'])
                    #email.send()

              #  except BadHeaderError: 
               #     return HttpResponse('Invalid header found.')
               # return HttpResponseRedirect('/contact/thanks/')    
            #else:
        # In reality we'd use a form class
        # to get proper validation errors.
             #   return HttpResponse('Make sure all fields are entered and valid.')
           # contact_form.save() 
        #return HttpResponseRedirect('/contact/')           
    return render(request, 'manage_contacts/contact.html', {'contact_form':contact_form,})

