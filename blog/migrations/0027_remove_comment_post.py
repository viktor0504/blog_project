# Generated by Django 4.2.1 on 2023-05-30 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]
