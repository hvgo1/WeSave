from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from manage_contacts.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import smtplib

#Sends all contacts to WeSave email
def contactUs(request):

    if request.method == 'GET': 
        contact_form = ContactForm()

    else:
        contact_form = ContactForm(request.POST)
  
        if contact_form.is_valid():
            #login admin
            gmail_user = settings.EMAIL_HOST_USER
            gmail_pwd = settings.EMAIL_HOST_PASSWORD

            TO = settings.EMAIL_WESAVE
            FROM_NAME = request.POST['name']
            MESSAGE = request.POST['message']
            CONTACT_EMAIL = request.POST['email']

            SUBJECT = "[Contact] from: %s " % FROM_NAME
            TEXT = "From : " +FROM_NAME+ "\n\n Email : " +CONTACT_EMAIL+ "\n\nMessage: " +MESSAGE+" \n" 
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            BODY = '\r\n'.join(['To: %s' % TO,
                'From: %s' % gmail_user,
                'Subject: %s' % SUBJECT,
                '', TEXT])

            server.sendmail(gmail_user, [TO], BODY)
            print ('email sent')            
            return HttpResponseRedirect('/home/')
    return render(request, 'manage_contacts/contact.html', {'contact_form':contact_form,})

