import re

class Email:
    def __init__(self):
        self.address = None
        self.__password__ = None
        self.port = None
        self.smtp = None

    def set_address(self,email):
        """ Set an email address to an account"""
        self.address = email
    
    def set_password(self,password):
        """ Set a password to an account."""
        self.__password__ = password

    def set_port(self,port):
        """ Set email port to be used for account"""
        self.port = port

    def set_smtp_server(self,address):
        self.smtp = address
    
    def check_email_format(self,email):
        """ Check if email is in right format """
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise Exception("Invalid email format")
        else:
            return "Email format is ok"

class Message:
    def __init__(self):
        self.receiver = None

    def set_receiver(self,email):
        """ Specify receipent of the email message """
        self.receiver = email
    
    def send_text_email(self,email,msg):
        """ Send a Plain-text email using SMTP_SSL """
        if msg == '1':
            raise Exception()

msg = Message()
msg.send_text_email(Email(),'hi')


