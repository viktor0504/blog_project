# Generated by Django 4.2.1 on 2023-06-23 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_remove_profile_pub_since'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pub_since',
            field=models.DateField(blank=True, null=True),
        ),
    ]
