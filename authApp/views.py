from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserProfileForm
from .models import Profile
import requests
from django.contrib.auth.hashers import make_password
import random
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.


def send_otp(number,message):
    url = "https://www.fast2sms.com/dev/bulk"
    api = "paste your api key here"
    querystring = {"authorization":api,"sender_id":"FSTSMS","message":message,"language":"english","route":"p","numbers":number}
    headers = {
        'cache-control': "no-cache"
    }
    return requests.request("GET", url, headers=headers, params=querystring)

    


def Registration(request):
    if request.method == "POST":
        fm = UserRegistrationForm(request.POST)
        up = UserProfileForm(request.POST)
        if fm.is_valid() and up.is_valid():
            e = fm.cleaned_data['email']
            u = fm.cleaned_data['username']
            p = fm.cleaned_data['password1']
            request.session['email'] = e
            request.session['username'] = u
            request.session['password'] = p
            p_number = up.cleaned_data['phone_number']
            request.session['number'] = p_number
            otp = random.randint(1000,9999)
            request.session['otp'] = otp
            message = f'your otp is {otp}'
            send_otp(p_number,message)
            return redirect('/registration/otp/')

    else:
        fm  = UserRegistrationForm()
        up = UserProfileForm()
    context = {'fm':fm,'up':up}
    return render(request,'registration.html',context)


def otpRegistration(request):
    if request.method == "POST":
        u_otp = request.POST['otp']
        otp = request.session.get('otp')
        user = request.session['username']
        hash_pwd = make_password(request.session.get('password'))
        p_number = request.session.get('number')
        email_address = request.session.get('email') 

        if int(u_otp) == otp:
            User.objects.create(
                            username = user,
                            email=email_address,
                            password=hash_pwd
            )
            user_instance = User.objects.get(username=user)
            Profile.objects.create(
                            user = user_instance,phone_number=p_number
            )
            request.session.delete('otp')
            request.session.delete('user')
            request.session.delete('email')
            request.session.delete('password')
            request.session.delete('phone_number')

            messages.success(request,'Registration Successfully Done !!')

            return redirect('/login/')
        
        else:
            messages.error(request,'Wrong OTP')


    return render(request,'registration-otp.html')


def userLogin(request):

    try :
        if request.session.get('failed') > 2:
            return HttpResponse('<h1> You have to wait for 5 minutes to login again</h1>')
    except:
        request.session['failed'] = 0
        request.session.set_expiry(100)



    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            request.session['username'] = username
            request.session['password'] = password
            u = User.objects.get(username=username)
            p = Profile.objects.get(user=u)
            p_number = p.phone_number
            otp = random.randint(1000,9999)
            request.session['login_otp'] = otp
            message = f'your otp is {otp}'
            send_otp(p_number,message)
            return redirect('/login/otp/')
        else:
            messages.error(request,'username or password is wrong')
    return render(request,'login.html')

def otpLogin(request):
    if request.method == "POST":
        username = request.session['username']
        password = request.session['password']
        otp = request.session.get('login_otp')
        u_otp = request.POST['otp']
        if int(u_otp) == otp:
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                request.session.delete('login_otp')
                messages.success(request,'login successfully')
                return redirect('/')
        else:
            messages.error(request,'Wrong OTP')
    return render(request,'login-otp.html')

def home(request):
    if request.method == "POST":
        otp = random.randint(1000,9999)
        request.session['email_otp'] = otp
        message = f'your otp is {otp}'
        user_email = request.user.email

        send_mail(
            'Email Verification OTP',
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )
        return redirect('/email-verify/')

    return render(request,'home.html')

def email_verification(request):
    if request.method == "POST":
        u_otp = request.POST['otp']
        otp = request.session['email_otp']
        if int(u_otp) == otp:
           p =  Profile.objects.get(user=request.user)
           p.email_verified = True
           p.save()
           messages.success(request,f'Your email {request.user.email} is verified now')
           return redirect('/')
        else:
            messages.error(request,'Wrong OTP')


    return render(request,'email-verified.html')