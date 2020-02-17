import re
import smtplib
import ssl

class Email:
    def __init__(self):
        self.address = None
        self.password = None
        self.port = None
        self.smtp = None
        self.username = None
        self.email_name = None
    def set_address(self,email):
        """ Set an email address to an account"""
        self.address = email
    def set_password(self,password):
        """ Set a password to an account."""
        self.password = password
    def set_port(self,port):
        """ Set email port to be used for account"""
        self.port = port
    def set_smtp_server(self,address):
        """ Set email server to be used for account"""
        self.smtp = address
    def set_username(self,username):
        """ Set username for account, maybe blank"""
        self.username = username
    def set_email_name(self,name):
        """ Set Name to be sent from"""
        self.email_name = name
    
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
    def send_text_email(self,email_account,message):
        with smtplib.SMTP(email_account.smtp, email_account.port) as server:
            server.login(email_account.username, email_account.password)
            server.sendmail(email_account.address, self.receiver, message)
    def send_ssl_text_email(self,email_account,message):
        context = ssl.create_default_context()
        with smtplib.SMTP(email_account.smtp, email_account.port) as server:
            server.starttls(context=context)
            server.login(email_account.username, email_account.password)
            server.sendmail(email_account.address, self.receiver, message)
