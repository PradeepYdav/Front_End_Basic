import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","first_project.settings")


import django
django.setup()

import random
from first_app.models import Topic,AceessRecord,Webpage
from faker import  Faker


fakergen= Faker()
topics=['Search','Social','Marketplace','Games','Music','News']

def add_topic():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()

    return t


def populate(N=5):

    for i in range(N):

        #get the topic for entry
        top= add_topic()

        # create the fake data for the entry
        fake_url=fakergen.url()
        fake_date=fakergen.date()
        fake_name=fakergen.company()

        # create the new webapage entry

        webpg=Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        acc_rec=AceessRecord.objects.get_or_create(name=webpg,date=fake_date)



if __name__== '__main__':
    print('populating script')
    populate(20)
    print("Populate Completed")
