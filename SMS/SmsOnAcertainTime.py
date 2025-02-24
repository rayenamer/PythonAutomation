import os
from twilio.rest import Client
import time
from datetime import datetime as dt

account_sid = 0
auth_token = 0
client = Client(account_sid, auth_token)

while True:
  now = dt.now()
  if now.hour == 13 and now.minute == 18:
    message = client.messages \
                    .create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='',
                        to=''
                    )

    print(message.sid)
  time.sleep(60)