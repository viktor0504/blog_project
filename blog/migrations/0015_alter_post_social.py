# Generated by Django 4.2.1 on 2023-05-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='social',
            field=models.CharField(max_length=50),
        ),
    ]
