from twilio.rest import Client

def send_sms(body, to_number):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_='+1234567890',
        to=to_number
    )