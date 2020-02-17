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
    def test_smtp(self):
        an_email = Email()
        an_email.set_smtp_server('smtp.gmail.com')
        self.assertEqual(an_email.smtp,'smtp.gmail.com')
    def test_email_format(self):
        an_email = Email()
        with self.assertRaises(Exception):
            an_email.check_email_format("email.com")
    def test_sender_email(self):
        msg = Message()
        msg.set_receiver('them@theiremail.com')
        self.assertEqual(msg.receiver,'them@theiremail.com')
    def test_send_text_email(self):
        an_email = Email()
        an_email.set_address('test.email@email.com')
        an_email.set_password('mypass')
        an_email.set_port(444)
        msg = Message()
        msg.set_receiver('email@email.com')
        my_message = "1"
        with self.assertRaises(Exception):
            msg.send_text_email(an_email, my_message)


if __name__ == '__main__':
    unittest.main()