from django import forms
from django.conf import settings
from django.core.mail import send_mail

from .models import Profile
from user.models import User



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



class UserSignupForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}))

    #Fields for profile
    nation = forms.ChoiceField(choices=NATIONALITY_CHOICES, required=False, widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(choices=SEX_CHOICES, required=False, widget=forms.Select(attrs={"class": "form-control"}))
    birth = forms.DateField(widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}))
    contact_inf = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Contact info"}))

    def send_registration_email(self, recipient):
        subject = "Confirm your signup to start blogging!"
        message = "This is your code verification!"
        sender = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, sender, [recipient], fail_silently=True)




    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data["password"]
        confirm_password = data["confirm_password"]

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return data



    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("The username must be unique")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("That email is already in use!")
        return email



    def save(self):
        user = User.objects.create_user(
            username = self.cleaned_data['username'].lower(),
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password'],
        )
        profile = Profile.objects.create(
            user=user,
            nation=self.cleaned_data['nation'],
            sex=self.cleaned_data['sex'],
            contact_inf=self.cleaned_data['contact_inf'],
            birth=self.cleaned_data['birth'],
        )

        return profile