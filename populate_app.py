import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()


import random

from blog.models import Post
from faker import Faker

fake = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_tag():
    t = Post.objects.get_or_create(tag=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        tag = add_tag()

        fake_title = fake.title()
        fake_name = fake.name()
        fake_content = fake.text()
        
        
        
        post = Post.objects.get_or_create(title=fake_title,
                                        author=fake_name,
                                        content=fake_content,
                                        tag=tag)


if __name__ == '__main__':
    populate(20)