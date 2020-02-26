import os
from twilio.rest import Client

account_sid = os.environ["AC305c6618726da7bb98419806610db628"]
auth_token = os.environ["6461f40481de49a44c7d5875c3ee7468"]

client = Client(account_sid, auth_token)

client.messages.create(
    to=os.environ["MY_PHONE_NUMBER"],
    from_="+12053464244",
    body="hello"
)

