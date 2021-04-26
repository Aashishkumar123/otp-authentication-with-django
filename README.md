# otp-authentication-with-django

So, hey guys this repositry is all about how to authenticate with mobile OTP Verification using django <br>

<img src="image/Screenshot 2021-04-26 at 5.40.54 PM.png">

<h6>Api that i used to send OTP</h6>
Go to this website https://www.fast2sms.com/ and just sigup and you will get the 50 bucks credit, that you could use to send sms.<br>
follow this link https://www.fast2sms.com/dashboard/dev-api and here you will get your api key just copy the api key and paste it views.py file of send_otp() function inside the api variable.

<h3>modules used </h3>
Django==3.0.5 --->> pip / pip3 install django <br>
requests==2.25.1 --->>> pip / pip3 install requests


 <h1> 1. Registration with OTP </h1><br>
 <p> Add your credintals and just click on create account</p> <br>
 
 
 <img src="https://github.com/Aashishkumar123/otp-authentication-with-django/blob/main/image/Screenshot%202021-04-26%20at%204.50.17%20PM.png" width="600px;">
 
 <br>
 <p> Now an OTP has been send to your mobile number copy the otp and paste it here</p> <br>
 <img src="https://github.com/Aashishkumar123/otp-authentication-with-django/blob/main/image/Screenshot%202021-04-26%20at%204.52.24%20PM.png" width="600px;">

<br><br>

<h1> 2. Login with OTP </h1><br>
 <p> Add your credintals and just click on Login</p> <br>
  <img src="https://github.com/Aashishkumar123/otp-authentication-with-django/blob/main/image/Screenshot%202021-04-26%20at%204.52.49%20PM.png" width="600px;">
  <br>
 <p> Now an OTP has been send to your regsitered mobile number copy the otp and paste it here</p> <br>
 <img src="https://github.com/Aashishkumar123/otp-authentication-with-django/blob/main/image/Screenshot%202021-04-26%20at%204.53.05%20PM.png" width="600px;">

<br><br>

<h5>Now you will redirect to  home page now click on verify now , you will get an email just copy the otp and paste it. <h5>
 <img src="image/Screenshot 2021-04-26 at 5.40.32 PM.png" width="600px;">




<h5>Now it redirect again to the home page but your email is verified now <h5>
 <img src="image/Screenshot 2021-04-26 at 4.53.17 PM.png" width="600px;">

 
 
 
 
