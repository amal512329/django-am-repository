import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','formmodel.settings')

import django
django.setup()

from faker import Faker
from formmodel_app.models import Adress

fakegen = Faker()

def populate(N=5):
    
    for entry in range(N):

        fake_name = fakegen.name().split()
        f_firstname  = fake_name[0]
        f_secondname = fake_name[1]
        email = fakegen.email()

        #creating the entry to the model

        user = Adress.objects.get_or_create(first_name=f_firstname,
                                            last_name=f_secondname,
                                            email_id = email)

if __name__ == '__main__':
    print('POPULATING STARTED')
    populate(20)
    print('POPULATION FINISHED')



