from django.db import models
from django.conf import settings


SEX_CHOICES = [
        ('-', '-'),
        ('M', 'M'),
        ('F', 'F'),
    ]

NATIONALITY_CHOICES = [
        ('-', '-'),
        ('V', 'V'),
        ('E', 'E'),
]



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile/',blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    contact_inf = models.CharField(max_length=150, blank=True, null=True)
    sex = models.CharField(choices=SEX_CHOICES, max_length=2, blank=True, null=True)
    nation = models.CharField(choices=NATIONALITY_CHOICES, max_length=2, blank=True, null=True)
    pub_since = models.DateField(blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    
    class Meta:
        app_label = 'profiles'

    def __str__(self):
        return self.user.username


        


