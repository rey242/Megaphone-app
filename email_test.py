import unittest
from email import *

class EmailTest(unittest.TestCase):
    def test_email_address(self):
        an_email = Email()
        an_email.set_address('test.email@email.com')
        self.assertEqual(an_email.address,'test.email@email.com')
    def test_password(self):
        an_email = Email()
        an_email.set_password('mypass')
        self.assertEqual(an_email.__password__ , 'mypass')
    def test_port(self):
        an_email = Email()
        an_email.set_port(444)
        self.assertEqual(an_email.port,444)

if __name__ == '__main__':
    unittest.main()