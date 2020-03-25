from app_email import Email, Message

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

This is a test e-mail message from SSL."""

message_open = f"""\
Subject: Hi Mailtrap - Open
To: {msg.receiver}
From: {em.email_name} <{em.address}>

This is a test e-mail message from Open."""

msg.send_text_email(em,message_open)

msg.send_ssl_text_email(em, message)
