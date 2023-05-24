# from django.shortcuts import render
# from .helpers import OtpHandler
# from django.contrib.auth import authenticate, login
# from .models import Customer
# from django.contrib.auth.models import User


# # Create your views here.

# def login_page(request):
#     return render(request, 'accounts/login.html')

# def login_handle(request):
#     user_name = request.POST.get('user_name')
#     password = request.POST.get('password')

#     user = authenticate(request,username=user_name, password=password)

#     if user is not None:
#         login(request, user)
#         return render(request, 'accounts/dashboard.html')
#     else:
#         return render(request, 'accounts/login.html', {'error': 'Invalid credentials.'})

# def register_handle(request):
#     email           = request.POST.get('email')
#     password        = request.POST.get('password')
#     phone_number    = request.POST.get('phone_number')
#     full_name       = request.POST.get('full_name')

#     user            = User.objects.create_user(email, password,first_name=full_name,username=phone_number,is_active=False)
#     otp             = OtpHandler(phone_number)
#     if otp.send_otp():
#         user.save()
#         return render(request, 'accounts/verify_otp.html')
#     else:
#         return render(request, 'accounts/register.html', {'error': 'OTP could not be sent.'})
    


# def register_page(request):
#     return render(request, 'accounts/register.html')



# def send_otp(request):
#     otp_obj = OtpHandler(request.POST.get('phone_number'))
#     if otp_obj.send_otp():
#         return render(request, 'accounts/verify_otp.html')
#     else:
#         return render(request, 'accounts/login.html', {'error': 'OTP could not be sent.'})

# def verify_otp(request):
#     otp_obj = OtpHandler(request.POST.get('phone_number'))
#     if otp_obj.verify_otp(request.POST.get('otp')):
#         return render(request, 'accounts/dashboard.html')
#     else:
#         return render(request, 'accounts/verify_otp.html', {'error': 'OTP could not be verified.'})


