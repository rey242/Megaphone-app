import unittest
from phone_pc import PcPhone

class SmsTest(unittest.TestCase):

    def test_account(self):
        sms = PcPhone()
        sms.set_account_sid('ACa00701c3867a69f3eef76f84bc7ddd5a')
        self.assertEqual(sms.get_account_sid(),'ACa00701c3867a69f3eef76f84bc7ddd5a')

    def test_auth_token(self):
        sms = PcPhone()
        sms.set_auth_token('64e14618a92ef536a354b97be1381986')
        self.assertEqual(sms.get_auth_token(),'64e14618a92ef536a354b97be1381986')

    def test_recip(self):
        sms = PcPhone()
        sms.set_recip('+18327386625')
        self.assertEqual(sms.recip,'+18327386625')
    
    def test_sender(self):
        sms = PcPhone()
        sms.set_sender('+12066811505')
        self.assertEqual(sms.sender,'+12066811505')

    def test_username(self):
        sms = PcPhone()
        sms.set_username('a_username')
        self.assertEqual(sms.username,'a_username')

    def test_recording(self):
        sms = PcPhone()
        sms.set_recording('recording.com')
        self.assertEqual(sms.recording,'recording.com')
    
    def test_voice_message(self):
        sms = PcPhone()
        sms.set_voice_message("my_voice.mp3")
        self.assertEqual(sms.voice_message,"my_voice.mp3")

    def test_twml(self):
        sms = PcPhone()
        sms.set_twml("https://rey242.github.io/download.xml")
        self.assertEqual(sms.twml,"https://rey242.github.io/download.xml")

    def test_call(self):
        sms = PcPhone()
        sms.set_username('a_username')
        sms.set_account_sid('ACa00701c3867a69f3eef76f84bc7ddd5a')
        sms.set_auth_token('64e14618a92ef536a354b97be1381986')
        sms.set_recip('+18327386625')
        sms.set_sender('+12066811505')
        #sms.set_twml("https://rey242.github.io/test.xml")
        sms.set_voice_message('<Response><Say>Ahoy, World!</Say></Response>')
        suc,sid = sms.call_recip()
        self.assertEqual(suc,'Call Sent.')

if __name__ == '__main__':
    unittest.main()