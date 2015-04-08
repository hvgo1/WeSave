# coding: utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from django.contrib.auth.models import User
from django_countries.fields import CountryField
from crowdsourcing.models import Region,City,Barangay,Wish,Keyword,Address,Service_Category,UserProfile,Individual,Group,Campaign,Campaign_User_Donor,Campaign_User_Followers,Campaign_Keyword,Unregistered_Donor,Contact,Campaign_Wish

def populate():

    add_barangay("Quiapo")
    add_barangay("Intramuros")
    add_barangay("Burgos")
    add_barangay("Almanza")
    add_barangay("Bangkal")
    add_barangay("Greenbelt")
    add_barangay("Pasay")
    add_barangay("Nangka")
    add_barangay("Mayamot")
    add_barangay("Aguho")
    print "brgy" 

    add_city("Marikina")
    add_city("Quezon")
    add_city("Las Pinas")
    add_city("Manila")
    add_city("Makati")
    add_city("Pasig")
    add_city("Pasay")
    add_city("Ilocos Sur")
    add_city("Taguig")
    add_city("Pateros")
    print "city" 

    add_region("Ilocos Region")
    add_region("Cagayan Valley")
    add_region("Central Luzon")
    add_region("CALABARZON")
    add_region("MIMAROPA")
    add_region("Bicol Region")
    add_region("Western Visayas")
    add_region("Eastern Visayas")
    add_region("Central Visayas")
    add_region("Zamboanga Peninsula")
    add_region("Northern Mindanao")
    add_region("Davao Region")
    add_region("SOCCSKARGEN")
    add_region("CARAGA")
    add_region("Cordillera Administrative Region")
    add_region("Autonomous Region for Muslim Mindanao")
    add_region("National Capital Region")
    print "reg" 

    add_sercat("Abuse")
    add_sercat("Animal")
    add_sercat("Arts")
    add_sercat("Cancer")
    add_sercat("Children")
    add_sercat("Chronic Illness")
    add_sercat("Civil Rights")
    add_sercat("Disability")
    add_sercat("Disaster Re‪lief")
    add_sercat("Education")
    add_sercat("Elderly")
    add_sercat("Emotional Support")
    add_sercat("Environment")
    add_sercat("Health")
    add_sercat("HIV and AIDS")
    add_sercat("Hospital and Hospice")
    add_sercat("Human Rights")
    add_sercat("Humanitarian Aid")
    add_sercat("Indegenous")
    add_sercat("Medical and Health")
    add_sercat("Music")
    add_sercat("Poverty")
    add_sercat("Refugees")
    add_sercat("Religion")
    add_sercat("Rescue")
    add_sercat("Social Welfare")
    add_sercat("Sports and Leisure")
    add_sercat("Welfare")
    add_sercat("Women")
    add_sercat("Youth")
    print "sercat" 

    add_keyword("Cancer") 
    add_keyword("AIDS") 
    add_keyword("Disability") 
    add_keyword("Medicine") 
    add_keyword("Equipment") 
    add_keyword("Bills")
    print "keyw" 

    add_wish("Wheelchair",'1')
    add_wish("Financial Assisstance",'0')
    add_wish("Medicine",'1')
    add_wish("Nebulizer",'1')
    add_wish("Walker",'1')
    add_wish("Diabetic shoes",'1')
    add_wish("Hospital bed",'1')
    add_wish("Crutch",'1') 
    print "wish" 

    add_address(street="36 Barangka St.",
        barangay=8,city=1,region=17,country='PH')
    add_address(street="57 Magdangal St.",
        barangay=3,city=8,region=1,country='PH')
    add_address(street="127 Rizal St.",
        barangay=5,city=5,region=17,country='PH')
    add_address(street="54 General Luna St.",
        barangay=1,city=2,region=17,country='PH')
    add_address(street="65 Roces St.",
        barangay=10,city=10,region=17,country='PH')
    add_address(street="52 Starlight St.",
        barangay=4,city=3,region=17,country='PH') 
    add_address(street="Higashi-Shiokōji 721-1, Shimogyō-ku, Kyōto-shi, Kyōto-fu 600-8216",
        barangay=None,city=None,region=None,country='JP') 
    add_address(street="73, Jalan Cilaki BANDUNG 40115",
        barangay=None,city=None,region=None,country='ID') 
    add_address(street="VIA APPIA NUOVA 123/4 00184 ROMA RM ",
        barangay=None,city=None,region=None,country='IT') 
    add_address(street="Flat D, 6/F, Golden Industrial Center, Block 4, 182-190 Tai Lin Pai Road,Kwai Chung",
        barangay=None,city=None,region=None,country='HK') 
    print "addr"
     
    add_user(uname="trisprior",
        passw="trisprior",
        email="tris@yahoo.com")
    add_user(uname="helpthechildren",
        passw="helpthechildren",
        email="helpthechildren@gmail.com")
    add_user(uname="emmaroberts",
        passw="emmaroberts",
        email="eroberts@gmail.com")
    add_user(uname="chrispine",
        passw="chrispine",
        email="cp@gmail.com")
    add_user(uname="sullichoi",
        passw="sullichoi",
        email="sc@gmail.com")
    add_user(uname="douglasbooth",
        passw="douglasbooth",
        email="dbooth213@gmail.com")
    add_user(uname="mirandakerr",
        passw="mirandakerr",
        email="kerrrr@gmail.com")
    add_user(uname="savethepoor",
        passw="savethepoor",
        email="savethepoor@yahoo.com")
    add_user(uname="carlasingson",
        passw="carlasingson",
        email="carsing@yahoo.com")
    add_user(uname="markdy",
        passw="markdy",
        email="dymark@yahoo.com")
    print "user" 

    add_userprof(photo="profile_images/4.jpg",
        address=1,
        user=11,
        role='Don')
    add_userprof(photo="profile_images/1.jpg",
        address=2,
        user=10,
        role='Don')
    add_userprof(photo="profile_images/3.jpg",
        address=3,
        user=9,
        role='Don')
    add_userprof(photo="profile_images/2.jpg",
        address=4,
        user=8,
        role='Adm')
    add_userprof(photo="profile_images/4.jpg",
        address=5,
        user=7,
        role='Ben')
    add_userprof(photo="profile_images/2.jpg",
        address=6,
        user=6,
        role='Hos')
    add_userprof(photo="profile_images/3.jpg",
        address=7,
        user=5,
        role='Ben')
    add_userprof(photo=None,
        address=8,
        user=4,
        role='Adm')
    add_userprof(photo="profile_images/1.jpg",
        address=9,
        user=3,
        role='Hos')
    add_userprof(photo=None,
        address=10,
        user=2,
        role='Don')
    print "uprof" 

    add_indiv(fname="Tris",mid=None,lname="Prior",bday="1991-01-04",user=2)
    add_indiv(fname="Emmalyn",mid="Santos",lname="Roberts",bday="1971-08-26",user=4)
    add_indiv(fname="Christopher",mid="Lopez",lname="Pine",bday="1961-06-30",user=5)
    add_indiv(fname="Sulli",mid=None,lname="Choi",bday="1963-04-18",user=6)
    add_indiv(fname="Douglas",mid="Kane",lname="Booth",bday="1993-10-07",user=7)
    add_indiv(fname="Miranda",mid="Scherzinger",lname="Kerr",bday="1982-09-02",user=8)
    add_indiv(fname="Carla",mid="Ong",lname="Singson",bday="1985-03-12",user=10)
    add_indiv(fname="Mark John",mid=None,lname="Dy",bday="1978-05-21",user=11)
    print "indiv" 

    add_group(name="Save the Poor",page="http://www.fb.com/savethepoor",
        abt="We help the poor",scat=[19],rnum=1200334,doc=None,comm=None,pcf="Mariz",pcl="Sumali",
        pce="mumali@gmail.com",pcj="President",pcp="09277779821",scf="Cristine",
        scl="Nueves",sce="cnueves@yahoo.com",scj="Secretary",scp="9981289",user=9)
    add_group(name="Help the Children Society",page="www.helpthechildren.com.ph",abt="Vestibulum tincidunt enim in pharetra malesuada. Duis semper magna metus electram accommodare",scat=[5,4],rnum=None,doc="documents/doc.pdf",
        comm="Government Document",pcf="Joseph",pcl="Alvarez",pce="jalvarez@hotmail.com",pcj="Head",pcp="09225672811",
        scf="Mario",scl="Lucas",sce="mario_lucas@gmail.com",scj="Director",scp="09052357778",user=3)

    add_campaign(title="For the Kids",beneficiary="Ella,Rosie,Marie,Selena",
        story="Vestibulum tincidunt enim in pharetra malesuada. Duis semper magna metus electram accommodare",
        dline="2015-06-28",status='D',views=10,ack=None,image="profile_images/2.jpg",createdby=2)
    print "grp" 

    add_campaign(title="Maura",beneficiary="Maura",
        story="Vestibulum tincidunt enim in pharetra malesuada. Duis semper magna metus electram accommodare",
        dline="2015-06-28",status='F',views=5,ack=None,image="profile_images/1.jpg",createdby=6)

    add_campaign(title="Ben",beneficiary="Ben",
        story="Vestibulum tincidunt enim in pharetra malesuada. Duis semper magna metus electram accommodare",
        dline="2015-06-28",status='V',views=0,ack=None,image="profile_images/1.jpg",createdby=3)

    add_campaign(title="Andy",beneficiary="Andy",
        story="Vestibulum tincidunt enim in pharetra malesuada. Duis semper magna metus electram accommodare",
        dline="2015-02-23",status='C',views=10,ack="ack_receipts/ack.pdf",image="profile_images/3.jpg",createdby=7)

    add_campaign(title="Lyn & Yve",beneficiary="Lyn, Yve",
        story="Vestibulum tincidunt enim in pharetra malesuada. Duis semper magna metus electram accommodare",
        dline="2011-06-28",status='I',views=10,ack=None,image="profile_images/1.jpg",createdby=4)
    print "camp" 

    add_unregdonor(name="Syara",campaign=1,amount=200.00)
    add_unregdonor(name="Casie",campaign=1,amount=2500.00)
    add_unregdonor(name="Jun",campaign=2,amount=600.00)
    add_unregdonor(name="Anonymous",campaign=4,amount=10.00)
    add_unregdonor(name="Anonymous",campaign=1,amount=200.00)
    add_unregdonor(name="Anonymous",campaign=4,amount=2500.00)
    add_unregdonor(name="Junie",campaign=2,amount=600.00)
    add_unregdonor(name="Anonymous",campaign=2,amount=10.00)
    add_unregdonor(name="Lyca",campaign=3,amount=200.00)
    add_unregdonor(name="Sophie Rey",campaign=1,amount=500.00)
    add_unregdonor(name="Jun Alden",campaign=2,amount=5.00)
    add_unregdonor(name="Anonymous",campaign=5,amount=10.00)

    add_contact(name="Aisa",email="ai@yahoo.com",msg="jsdasfnadnfdfna")
    add_contact(name="Riz",email="rizalee@yahoo.com",msg="jsdasfnadnfdfna")
    add_contact(name="Ms. Claire Danes",email="danesclaire@yahoo.com",msg="jsdasfnadnfdfna")
    add_contact(name="Ernie Calungsod",email="ai@yahoo.com",msg="jsdasfnadnfdfna")
    add_contact(name="Paul Diaz",email="pdiaz@yahoo.com",msg="jsdasfnadnfdfna")
    add_contact(name="Henry Jose",email="henjos@yahoo.com",msg="jsdasfnadnfdfna")
    add_contact(name="Nica Jane",email="nj@yahoo.com",msg="jsdasfnadnfdfna")
    add_contact(name="Missi Lee",email="mlee@yahoo.com",msg="jsdasfnadnfdfna")
    add_contact(name="Jenne Fuentes",email="jf@yahoo.com",msg="jsdasfnadnfdfna")
    add_contact(name="Suzy Bae",email="sz@yahoo.com",msg="jsdasfnadnfdfna")
    print "unreg" 

    add_campdonor(campaign=1,user=2,amount=700.00)
    add_campdonor(campaign=1,user=9,amount=740.00)
    add_campdonor(campaign=1,user=6,amount=300.00)
    add_campdonor(campaign=1,user=11,amount=700.00)
    add_campdonor(campaign=1,user=10,amount=740.00)
    add_campdonor(campaign=2,user=2,amount=100.00)
    add_campdonor(campaign=2,user=6,amount=800.00)
    add_campdonor(campaign=2,user=9,amount=100.00)
    add_campdonor(campaign=2,user=11,amount=800.00)
    add_campdonor(campaign=3,user=10,amount=700.00)
    add_campdonor(campaign=3,user=2,amount=740.00)
    add_campdonor(campaign=3,user=6,amount=700.00)
    add_campdonor(campaign=3,user=9,amount=740.00)
    add_campdonor(campaign=4,user=11,amount=300.00)
    add_campdonor(campaign=4,user=2,amount=100.00)
    add_campdonor(campaign=4,user=6,amount=300.00)
    add_campdonor(campaign=4,user=9,amount=100.00)
    add_campdonor(campaign=5,user=10,amount=800.00)
    add_campdonor(campaign=5,user=11,amount=800.00)
    print "cdon" 

    add_campwish(campaign=1,wish=1,compl=0,est=5000.00)
    add_campwish(campaign=2,wish=3,compl=0,est=3000.00)
    add_campwish(campaign=3,wish=4,compl=1,est=1000.00)
    add_campwish(campaign=4,wish=5,compl=0,est=2000.00)
    add_campwish(campaign=5,wish=6,compl=0,est=4000.00)
    add_campwish(campaign=1,wish=5,compl=0,est=2000.00)
    add_campwish(campaign=2,wish=3,compl=0,est=1500.00)
    add_campwish(campaign=3,wish=8,compl=1,est=1300.00)  
    print "cwish"     

    add_campfollowers(campaign=1,user=2)
    add_campfollowers(campaign=1,user=3)
    add_campfollowers(campaign=1,user=4)
    add_campfollowers(campaign=1,user=5)
    add_campfollowers(campaign=2,user=6)
    add_campfollowers(campaign=2,user=7)
    add_campfollowers(campaign=2,user=8)
    add_campfollowers(campaign=2,user=9)
    add_campfollowers(campaign=3,user=10)
    add_campfollowers(campaign=3,user=11)
    add_campfollowers(campaign=4,user=2)
    add_campfollowers(campaign=4,user=4)
    add_campfollowers(campaign=5,user=9)
    add_campfollowers(campaign=5,user=10)
    print "cfoll" 

    add_campkey(campaign=1,keyw=1) 
    add_campkey(campaign=1,keyw=2) 
    add_campkey(campaign=2,keyw=3) 
    add_campkey(campaign=2,keyw=5) 
    add_campkey(campaign=3,keyw=6) 
    add_campkey(campaign=5,keyw=1) 
    add_campkey(campaign=4,keyw=2) 
    add_campkey(campaign=1,keyw=3) 
    add_campkey(campaign=4,keyw=4) 
    add_campkey(campaign=5,keyw=4) 
    print "ckey" 

def add_city(name):
    c = City.objects.get_or_create(name=name)[0]
    return c

def add_barangay(name):
    b = Barangay.objects.get_or_create(name=name)[0]
    return b

def add_region(name):
    r = Region.objects.get_or_create(name=name)[0]
    return r

def add_sercat(name):
    s = Service_Category.objects.get_or_create(name=name)[0]
    return s

def add_keyword(name):
    k = Keyword.objects.get_or_create(name=name)[0]
    return k

def add_wish(name,wtype):
    w = Wish.objects.get_or_create(name=name,
        wish_type=wtype)[0]
    return w

def add_address(street,barangay,city,region,country):
    a = Address.objects.get_or_create(country=country,
        region_id=region, 
        city_id=city,
        barangay_id=barangay,
        street=street)[0]
    return a

def add_user(uname,passw,email):
    u = User.objects.get_or_create(username=uname,
        password=passw, 
        email=email)[0]
    return u
 
def add_userprof(photo,address,user,role):
    if photo==None:
        photo='profile_images/def.jpg'
    u = UserProfile.objects.get_or_create(photo=photo,
        address_id=address,
        user_id=user, 
        role=role)[0]
    return u

def add_indiv(fname,mid,lname,bday,user):
    u = Individual.objects.get_or_create(first_name=fname, 
        middle_name=mid,
        last_name=lname, 
        birthday=bday,
        user_id=user)[0]
    return u

def add_group(name,page,abt,scat,rnum,doc,comm,pcf,pcl,pce,pcj,pcp,scf,scl,sce,scj,scp,user):
    u = Group.objects.get_or_create(name=name,
        page_address=page,
        about=abt,
        
        registration_number=rnum,
        document=doc,
        comments=comm,
        pc_first_name=pcf,
        pc_last_name=pcl,
        pc_email=pce,
        pc_job_title=pcj,
        pc_phone_number=pcp,
        sc_first_name=scf,
        sc_last_name=scl,
        sc_email=sce,
        sc_job_title=scj,
        sc_phone_number=scp,
        user_id=user)[0]
    u.service_category.add(*scat)
    return u

def add_campaign(title,beneficiary,story,dline,status,views,ack,image,createdby):
    c = Campaign.objects.get_or_create(title=title,
        beneficiary_name=beneficiary,
        story=story,
        deadline=dline,
        status=status,
        views=views,
        ack_receipt=ack,
        campaign_image=image,
        created_by_id=createdby)[0]
    return c

def add_unregdonor(name,campaign,amount):
    c = Unregistered_Donor.objects.get_or_create(name=name,
        campaign_id=campaign,
        amount=amount)[0]
    return c

def add_contact(name,email,msg):
    c = Contact.objects.get_or_create(name=name,
        email=email,
        message=msg)[0]
    return c

def add_campdonor(campaign,user,amount):
    c = Campaign_User_Donor.objects.get_or_create(
        campaign_id=campaign,
        user_id=user,
        amount=amount)[0]
    return c

def add_campwish(campaign,wish,compl,est):
    c = Campaign_Wish.objects.get_or_create(
        campaign_id=campaign,
        wish_id=wish,
        completed=compl,
        estimated_price=est)[0]
    return c

def add_campfollowers(campaign,user):
    c = Campaign_User_Followers.objects.get_or_create(
        campaign_id=campaign,
        user_id=user)[0]
    return c

def add_campkey(campaign,keyw):
    c = Campaign_Keyword.objects.get_or_create(
        campaign_id=campaign,
        keyword_id=keyw)[0]
    return c


# Start execution here!
if __name__ == "__main__":
    print "Starting Crowdsourcing population script..."
    populate()
