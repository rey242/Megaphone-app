import unittest
from texting_pc import PcTexting

class SmsTest(unittest.TestCase):
    
    def test_account(self):
        sms = PcTexting()
        sms.set_account_sid('ACa00701c3867a69f3eef76f84bc7ddd5a')
        self.assertEqual(sms.account_sid,'ACa00701c3867a69f3eef76f84bc7ddd5a')

    def test_auth_token(self):
        sms = PcTexting()
        sms.set_auth_token('64e14618a92ef536a354b97be1381986')
        self.assertEqual(sms.auth_token,'64e14618a92ef536a354b97be1381986')
        
    def test_recip(self):
        sms = PcTexting()
        sms.set_recip('+18327386625')
        self.assertEqual(sms.recip,'+18327386625')

    def test_sender(self):
        sms = PcTexting()
        sms.set_sender('+12066811505')
        self.assertEqual(sms.sender,'+12066811505')

    def test_message(self):
        sms = PcTexting()
        sms.set_message('This is a trial message!')
        self.assertEqual(sms.message,'This is a trial message!')

    def test_callback(self):
        sms = PcTexting()
        sms.set_status_callback('https://postb.in/1584499976311-4565684816334')
        self.assertEqual(sms.status_callback,'https://postb.in/1584499976311-4565684816334')

    def test_sending_text(self):
        sms = PcTexting()
        sms.set_account_sid('ACa00701c3867a69f3eef76f84bc7ddd5a')
        sms.set_auth_token('64e14618a92ef536a354b97be1381986')
        sms.set_recip('+18327386625')
        sms.set_sender('+12066811505')
        sms.set_message('This is a trial message!')
        sms.set_status_callback('https://postb.in/1584499976311-4565684816334')
        result,sid = sms.send_text_message()
        self.assertEqual(result,"Message Sent")


if __name__ == '__main__':
    unittest.main()