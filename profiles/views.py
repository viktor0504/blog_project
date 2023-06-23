from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.views.generic import DetailView

from .models import Profile
from .forms import UserSignupForm
from user.models import User



class UserDetailView(DetailView):
    model = User
    template_name = 'profile/user_detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')  # Retrieve the username from URL parameter
        return self.model.objects.get(username=username)



class UserSignUpView(FormView):
    model = Profile
    form_class = UserSignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print(form.cleaned_data)
        recipient = form.cleaned_data['email']
        form.send_registration_email(recipient)
        form.save()
        return super().form_valid(form)




class UserLoginView(LoginView):
    template_name = 'registration/login.html'  # Replace with your login template

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me', None)
        if remember_me:
            self.request.session.set_expiry(1209600)  # Remember the user for two weeks
        return super().form_valid(form)



class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home') 