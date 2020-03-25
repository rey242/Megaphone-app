from twilio.rest import Client
import keyring

class PcTexting:
    def __init__(self):
        self.username = 'default'
        self.auth_token = None
        self.recip = None
        self.sender = None
        self.message = None
        self.mms_server = None
        self.post_server = None
        self.status_callback = None

    def set_account_sid(self, sid):
        keyring.set_password('Megaphone',self.username + '-sid',sid)
    
    def set_auth_token(self, token):
        keyring.set_password('Megaphone',self.username + '-auth',token)

    def get_account_sid(self):
        return keyring.get_password('Megaphone',self.username + '-sid')

    def get_auth_token(self):
        return keyring.get_password('Megaphone',self.username + '-auth')

    def set_username(self,name):
        self.username = name

    def set_recip(self, recip):
        self.recip = recip

    def set_sender(self, sender):
        self.sender = sender
    
    def set_message(self, message):
        self.message = message

    def set_status_callback(self, sc):
        self.status_callback = sc

    def send_text_message(self):
        client = Client(self.get_account_sid(), self.get_auth_token())
        msg = client.messages.create(
            to=self.recip,
            from_=self.sender,
            status_callback=self.status_callback,
            body=self.message
            
        )
        return "Message Sent.",msg