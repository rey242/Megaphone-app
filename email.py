
class Email:
    def __init__(self):
        self.address = None
        self.__password__ = None
        self.port = None

    def set_address(self,email):
        """ Set an email address to an account"""
        self.address = email
    
    def set_password(self,password):
        """ Set a password to an account."""
        self.__password__ = password

    def set_port(self,port):
        """ Set email port to be used for account"""
        self.port = port
    