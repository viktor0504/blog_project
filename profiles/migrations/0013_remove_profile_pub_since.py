# Generated by Django 4.2.1 on 2023-06-23 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_remove_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pub_since',
        ),
    ]
