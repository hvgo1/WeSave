from registration.forms import RegistrationFormNoFreeEmail

class RegistrationFormNoFreeEmail(RegistrationForm):
     
    bad_domains = ['aim.com', 'aol.com', 'email.com','hushmail.com',
                   'mail.ru', 'mailinator.com', 'live.com']
