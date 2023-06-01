from django.urls import path

from .views import UserSignUpView, UserLoginView, UserLogoutView, UserDetailView

app_name='profile'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='profile_login'),
    path('signup/', UserSignUpView.as_view(), name='profile_signup'),
    path('logout/', UserLogoutView.as_view(), name='profile_logout'),
    path('user/<str:username>/', UserDetailView.as_view(), name='user_detail'),

]