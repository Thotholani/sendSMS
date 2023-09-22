import json
from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings
from django.http import HttpResponse

def send_sms(request):
    receivedEmail = ''
    receivedPassword = ''
    receivedNumber = ''


    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        receivedEmail = data.get('email')
        receivedPassword = data.get('password')
        receivedNumber = data.get('number')

    # Your Twilio credentials
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_number = settings.TWILIO_PHONE_NUMBER

    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # User's phone number (replace with the actual phone number)
    to_phone_number = receivedNumber

    # Email and password from authentication form
    email = receivedEmail
    password = receivedPassword

    # Message to be sent
    message_body = f'Hello. Your account has been created. To access the Dawa Mom App use the email and password credential provided. Please do not share these credentials with anyone.\n Email: {email}\nPassword: {password}'

    try:
        # Send the SMS
        message = client.messages.create(
            body=message_body,
            from_='Dawa Mom',  # Your Twilio phone number
            to=to_phone_number
        )
        return HttpResponse(f'SMS sent successfully to {to_phone_number}. Message SID: {message.sid}')
    except Exception as e:
        return HttpResponse(f'Failed to send SMS: {str(e)}')
