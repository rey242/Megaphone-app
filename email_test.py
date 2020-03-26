import unittest
from app_email import Email, Message


class EmailTest(unittest.TestCase):
    def test_email_address(self):
        an_email = Email()
        an_email.set_address('test.email@email.com')
        self.assertEqual(an_email.address, 'test.email@email.com')

    def test_password(self):
        an_email = Email()
        an_email.set_password('mypass')
        self.assertEqual(an_email.password, 'mypass')

    def test_port(self):
        an_email = Email()
        an_email.set_port(444)
        self.assertEqual(an_email.port, 444)

    def test_smtp(self):
        an_email = Email()
        an_email.set_smtp_server('smtp.gmail.com')
        self.assertEqual(an_email.smtp, 'smtp.gmail.com')

    def test_sender_email(self):
        msg = Message()
        msg.set_receiver('them@theiremail.com')
        self.assertEqual(msg.receiver, 'them@theiremail.com')

    def test_send_text_email(self):
        em = Email()
        msg = Message()

        msg.set_receiver("to@smtp.mailtrap.io")
        em.set_address("from@smtp.mailtrap.io")
        em.set_smtp_server("smtp.mailtrap.io")
        em.set_port(2525)
        em.set_username("c123d2a294f857")
        em.set_password("07dc82c500f623")
        em.set_email_name('A user')
        
        message = f"""\
        Subject: Help! Something is Wrong!
        To: {msg.receiver}
        From: {em.email_name} <{em.address}>
            
        Help! Something is Wrong!."""
        
        self.assertEqual(msg.send_text_email(em, message),"Message Sent")
    
    def test_send_ssl_text_email(self):
        em = Email()
        msg = Message()

        msg.set_receiver("to@smtp.mailtrap.io")
        em.set_address("from@smtp.mailtrap.io")
        em.set_smtp_server("smtp.mailtrap.io")
        em.set_port(2525)
        em.set_username("c123d2a294f857")
        em.set_password("07dc82c500f623")
        em.set_email_name('A user')
        
        message = f"""\
        Subject: Hi Mailtrap - SSL email
        To: {msg.receiver}
        From: {em.email_name} <{em.address}>
            
        This is a test e-mail message with SSL."""
        
        self.assertEqual(msg.send_ssl_text_email(em, message),"Message Sent")


if __name__ == '__main__':
    unittest.main()
