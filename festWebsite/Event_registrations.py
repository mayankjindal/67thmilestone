import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'festWebsite.settings')
import django
django.setup()
import pandas as pa
import csv
from website.models import Events,single_event,event_register,Team_details,User,UserProfile
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def create():
    a = list(Events.objects.all())
    print (a)
    for i in a:
        print (i.name,i.contact_email1,i.contact_email2)
        if i.max_participants>1:
            b = list(event_register.objects.filter(event_name=i.name))
            e=[]
            for j in b:
                c=[]
                c.append(j.team_name)
                d = list(Team_details.objects.filter(event_name=i.name, team_name=j.team_name))
                for k in d:
                    c.append(k.name)
                    c.append(k.email)
                    c.append(k.phone)
                for l in range(len(d), i.max_participants):
                    c.append("")
                    c.append("")
                    c.append("")
                e.append(c)
            labels=["Team Name"]
            for k in range(0,i.max_participants):
                labels.append("Member"+str(k+1)+"Name")
                labels.append("Member" + str(k + 1) + "Email")
                labels.append("Member" + str(k + 1) + "Phone")
            df = pa.DataFrame(e, columns=labels)
            df.to_csv(i.name + ".csv")
            subject = "Registration File"
            body = u"Find the attached CSV File for registered participants for your event"+i.name
            emailsend = EmailMessage(subject, body, to=['pprashant2398@gmail.com'])
            path = os.getcwd()
            path += "/" + i.name + ".csv"
            emailsend.attach_file(path)
            emailsend.send()
        else:
            labels = ['Name', 'Email', 'Username', 'College Name', 'Contact Number', 'Gender']
            b=list(single_event.objects.filter(event_name=i.slug))
            e=[]
            for j in b:
                f=[]
                c = list(User.objects.all())
                for k in c:
                    if k.username==j.username:
                        break
                d = list(UserProfile.objects.filter(user=k))
                for l in d:
                    f.append(l.name)
                    f.append(k.email)
                    f.append(k.username)
                    f.append(l.college)
                    f.append(l.contact)
                    if l.gender == '0':
                        f.append("Female")
                    elif l.gender == '1':
                        f.append("Male")
                    elif l.gender == '2':
                        f.append("Other")
                e.append(f)
            g = []
            for m in e:
                if len(m) > 0:
                    g.append(m)
            df = pa.DataFrame(g, columns=labels)
            df.to_csv(i.name+".csv")
            subject = "Registration File"
            body = u"Find the attached CSV File for registered participants for your event"+i.name
            emailsend = EmailMessage(subject, body, to=['pprashant2398@gmail.com'])
            path = os.getcwd()
            path += ("/"+i.name+".csv")
            emailsend.attach_file(path)
            emailsend.send()

if __name__ == "__main__":
    print("Starting fetching database : ")
    create()