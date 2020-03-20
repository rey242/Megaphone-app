from twilio.rest import Client

class PcTexting:
    def __init__(self):
        self.account_sid = None
        self.auth_token = None
        self.recip = None
        self.sender = None
        self.message = None
        self.mms_server = None
        self.post_server = None
        self.status_callback = None

    def set_account_sid(self, sid):
        self.account_sid = sid
    
    def set_auth_token(self, token):
        self.auth_token = token

    def set_recip(self, recip):
        self.recip = recip

    def set_sender(self, sender):
        self.sender = sender
    
    def set_message(self, message):
        self.message = message

    def set_status_callback(self, sc):
        self.status_callback = sc

    def send_text_message(self):
        client = Client(self.account_sid, self.auth_token)
        msg = client.messages.create(
            to=self.recip,
            from_=self.sender,
            status_callback=self.status_callback,
            body=self.message
            
        )
        return "Message Sent",msg