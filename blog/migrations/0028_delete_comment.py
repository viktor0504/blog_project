# Generated by Django 4.2.1 on 2023-05-30 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_remove_comment_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
