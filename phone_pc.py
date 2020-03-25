from twilio.rest import Client 
import keyring

class PcPhone:
    def __init__(self):
        self.username = 'default'
        self.account_sid = None
        self.auth_token = None
        self.recip = None
        self.sender = None
        self.recording = None
        self.voice_message = None
        self.twml = None

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

    def set_recording(self,record):
        self.recording = record
    
    def set_voice_message(self,msg):
        self.voice_message = msg

    def set_twml(self,twmil):
        self.twml = twmil

    def call_recip(self):
        client = Client(self.get_account_sid(), self.get_auth_token())
        call = client.calls.create(
            to=self.recip,
            from_=self.sender,
            url=self.twml,
            twiml= self.voice_message,
            method='GET'
        )
        return 'Call Sent.',call.sid