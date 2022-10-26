from twilio.rest import Client

TWILIO_SID = "ACf772fa6713b8985ef23c5b838c8bdae3"
TWILIO_AUTH_TOKEN = "5f624f631e4b92a2bdca8894957f8e67"
TWILIO_VIRTUAL_NUMBER = "+18142613653"
TWILIO_VERIFIED_NUMBER = "+14805282664"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)