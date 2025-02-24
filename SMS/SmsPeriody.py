import os
from twilio.rest import Client
import time

account_sid =0
auth_token = 0
client = Client(account_sid, auth_token)

while True:
  message = client.messages \
                  .create(
                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                      from_='',
                      to=''
                  )

  print(message.sid)
  time.sleep(60)