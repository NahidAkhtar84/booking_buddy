from twilio.rest import Client


def twilioSMS(body, address):
    account_sid = 'AC9accc9ed9d9a7be45bffd53462e4e3eb'
    auth_token = '4ae53d458c93ed085cdbd8c55059c575'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MG5db03c1845adb9501e3ff2eca70d4b44',
        body=body,
        to=address
    )

    print(message.sid)
