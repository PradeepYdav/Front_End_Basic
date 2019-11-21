import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()


from second_app.models import users
from faker import Faker
fake_gen=Faker()


def make_users(N=5):
     for i in range(N):
         f_name=fake_gen.name()
         l_name=fake_gen.name()
         email=fake_gen.email()

         users.objects.get_or_create(first_name=f_name,last_name=l_name,email=email)

if __name__=='__main__':
    print("Populated script start")
    make_users(20)
    print('populated script end ')
