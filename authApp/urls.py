from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home,name="home"),
    path('registration/',views.Registration, name="Registration"),
    path('registration/otp/',views.otpRegistration, name="otp-Registration"),
    path('login/',views.userLogin, name="user-login"),
    path('login/otp/',views.otpLogin, name="otp-login"),
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html')),
    path('email-verify/', views.email_verification, name="email-verify"),
    path('forget-password/',views.forget_password,name="forger-password"),
    path('forget-password/done/',TemplateView.as_view(template_name='forget-password-done.html')),
    path('change-password/<slug:uid>/',views.change_password,name="change-password"),
    
]
