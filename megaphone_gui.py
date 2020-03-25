from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from app_email import Email, Message

class MyGrid(Widget):
    pass

class MegaphoneApp(App):
    def build(self):
        return MyGrid()

    def on_press_button(self):
        em = Email()
        msg = Message()

        msg.set_receiver("to@smtp.mailtrap.io")
        em.set_address("from@smtp.mailtrap.io")
        em.set_smtp_server("smtp.mailtrap.io")
        em.set_port(2525)
        em.set_username("c123d2a294f857")
        em.set_password("07dc82c500f623")
        em.set_email_name('Rey')
        message = f"""\
Subject: Hi Mailtrap - SSL
To: {msg.receiver}
From: {em.email_name} <{em.address}>

This is a test e-mail message from SSL. Hi from Kivy too!"""

        message_open = f"""\
Subject: Hi Mailtrap - Open
To: {msg.receiver}
From: {em.email_name} <{em.address}>

This is a test e-mail message from Open. Hi from Kivy too!"""

        msg.send_text_email(em,message_open)

        msg.send_ssl_text_email(em, message)
        print('Email Sent!')

if __name__ == '__main__':
    app = MegaphoneApp()
    app.run()