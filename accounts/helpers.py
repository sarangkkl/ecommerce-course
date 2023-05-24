from firebase_admin import auth,credentials
import firebase_admin

class OtpHandler:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send_otp(self):
        try:
            auth.generate_phone_auth_code(self.phone_number)
            
            return True
        except Exception as e:
            return False

    def verify_otp(self, otp):
        try:
            user = auth.get_user_by_phone_number(self.phone_number, otp)
            credential = auth.PhoneAuthProvider.credential(user.uid, otp)
            auth.sign_in_with_credential(credential)
            return True
        except Exception as e:
            return False


class EmailHandler:
    def __init__(self, email):
        self.email = email

    def send_otp(self):
        try:
            auth.generate_email_verification_link(self.email)
            return True
        except Exception as e:
            return False

    def verify_otp(self, otp):
        try:
            user = auth.get_user_by_email(self.email)
            credential = auth.EmailAuthProvider.credential(user.uid, otp)
            auth.sign_in_with_credential(credential)
            return True
        except Exception as e:
            return False

# class NotificationHandler:
#     def __init__(self):
#         # Initialize Firebase Admin SDK
#         cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
#         firebase_admin.initialize_app(cred)

#         # Initialize Twilio client
#         account_sid = 'your_account_sid'
#         auth_token = 'your_auth_token'
#         self.client = Client(account_sid, auth_token)

#     def send_sms(self, phone_number, message):
#         # Send the SMS message using Twilio
#         message = self.client.messages \
#             .create(
#                 body=message,
#                 from_='your_twilio_phone_number',
#                 to=phone_number
#             )

#         return message.sid
