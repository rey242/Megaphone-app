import address_book
import app_email
import phone_pc
import texting_pc
import pyfiglet
import pickle

def header():
    ascii_banner = pyfiglet.figlet_format("Megaphone App")
    print(ascii_banner)


def main_menu():
    header()

    while True:
        print('\n')
        print('Choose from the following options')
        print('1. Select Messaging Options')
        print('2. Select Recipients')
        print('3. Enter Message')
        print('4. Send')
        print('5. Settings')
        print('6. Access Address Book')
        print('7. Quit')
        choice = input('> ')

        if choice in ('1','2','3','4','5','6','7'):
            return choice 
        else:
            print('Option not recognized, try again!')

def messaging_options():
    choice_list = []
    while True:
        print('\n')
        print('Choose from the following Messaging options')
        print('1. Text')
        print('2. Email')
        print('3. Phone')
        print('4. Return to main')
        choice = input('> ')

        if choice in ('1','2','3'):
            if choice in choice_list:
                print('Option already selected. Try again!')
                continue
            choice_list.append(choice)
        elif choice == '4':
            return choice_list
        else:
            print('Option not recognized, try again!')
            continue
        print('Add another Messaging option?')
        print('1. Yes')
        print('2. No')
        choice = input('> ')
        if choice == '1':
            continue
        else:
            return choice_list

def recip_select(book):
    recip_list = []
    if book.book == {}:
        print ('Address Book empty, please add entries before continuing.')
        return recip_list
    while True:
        print('Available Recipients:')
        recips = list(book.book.keys())
        for n,r in enumerate(recips):
            print('{}. {}'.format(n+1,r))
        
        print('\n')
        print('Choose from the following options')
        print('1. Add a recipient')
        print('2. Remove a recipient')
        print('3. Return to main')
        choice = input('> ')

        if not choice in ('1','2','3'):
            print('Option not recognized, try again!')
            continue
        else:
            if choice == '1':
                while True:
                    a_selection = input('Which recipient? > ')
                    if not a_selection.isnumeric():
                        print('Option not recognized, try again!')
                        continue
                    elif int(a_selection) > len(recips) or int(a_selection) < 1:
                        print('Selection not valid, try again!')
                        continue
                    else:
                        recip_list.append(book.get_entry(recips[int(a_selection)-1]))
                        break

            if choice == '2':
                while True:
                    if len(recip_list) == 0:
                        print('Recipient list is empty.')
                        break
                    for n,r in enumerate(recip_list):
                        print('{}. {}'.format(n+1,r))
                    a_selection = input('Which recipient to delete? > ')
                    if not a_selection.isnumeric():
                        print('Option not recognized, try again!')
                        continue
                    elif a_selection > len(recip_list) or a_selection < 1:
                        print('Selection not valid, try again!')
                        continue
                    else:
                        del recip_list[int(a_selection)]
                        break

            if choice == '3':
                return recip_list

def access_address_book(book):
    while True:
        print('\n')
        print('Contacts:')
        recips = list(book.book.keys())
        for n,r in enumerate(recips):
            print('{}. {}'.format(n+1,r))
        
        print('\n')
        print('Choose from the following options')
        print('1. Add a contact')
        print('2. Remove a contact')
        print('3. Return to main')
        choice = input('> ')
        
        if not choice in ('1','2','3'):
            print('Option not recognized, try again!')
            continue
        else:
            if choice == '1':
                while True:
                    a_selection = input('Name of Contact? > ')
                    try_name = book.add_entry(a_selection)
                    if not try_name:
                        print('Name not accepted, try again.')
                        continue
                    else:
                        entry = book.get_entry(a_selection)
                        while True:
                            a_selection = input('Email? > ')
                            try_email = entry.set_email(a_selection)
                            if not try_email:
                                print('Email not accepted, try again.')
                                continue
                            else:
                                break
                        while True:
                            b_selection = input('Cell Phone? (Enter Nothing if skipping) > ')
                            try_c = entry.set_cell_phone(b_selection)
                            if not try_c:
                                print('Cell Phone not accepted, try again.')
                                continue
                            else:
                                break
                        while True:
                            c_selection = input('Home Phone? (Enter Nothing if skipping) > ')
                            try_h = entry.set_home_phone(c_selection)
                            if not try_h:
                                print('Home Phone not accepted, try again.')
                                continue
                            else:
                                break
                        while True:
                            d_selection = input('Office Phone? (Enter Nothing if skipping) > ')
                            try_o = entry.set_office_phone(d_selection)
                            if not try_o:
                                print('Office Phone not accepted, try again.')
                                continue
                            else:
                                break
                        break
                with open('app_address_book.pkl', 'wb') as out:
                    pickle.dump(book,out, pickle.HIGHEST_PROTOCOL)
            if choice == '2':
                print('Contacts:')
                recips = list(book.book.keys())
                for n,r in enumerate(recips):
                    print('{}. {}'.format(n+1,r))
                    while True:
                        choice = input('Remove which contact? (Press q to quit) > ')
                        if choice.lower() == 'q':
                            break
                        if not choice.isnumeric():
                            print('Option not recognized, try again!')
                            continue
                        elif int(choice) > len(recips) or int(choice) < 1:
                            print('Selection not valid, try again!')
                            continue
                        while True:
                            choice1 = input('Are you sure? (y or n) > ')
                            if choice1.lower() == 'y':
                                book.delete_entry(recips[int(choice)-1])
                                break
                            elif choice1.lower() == 'n':
                                break
                            else:
                                print('Option not recognized, try again!')
                        break
                with open('app_address_book.pkl', 'wb') as out:
                        pickle.dump(book,out, pickle.HIGHEST_PROTOCOL)
            if choice == '3':
                return


def enter_message():
    msg = input('Please enter message you would like to send: >')
    return msg


def settings():
    print('Modify settings via pickle - Future feature!')
    return

def send_messages(msg_choice, msg_1):
    for m in msg_choice:
        if m == '1':
            sms = texting_pc.PcTexting()
            sms.set_account_sid('ACa00701c3867a69f3eef76f84bc7ddd5a')
            sms.set_auth_token('64e14618a92ef536a354b97be1381986')
            sms.set_recip('+18327386625')
            sms.set_sender('+12066811505')
            sms.set_message(msg_1)
            sms.set_status_callback('https://postb.in/1584499976311-4565684816334')
            result,sid = sms.send_text_message()
            print(result + ' - SMS')
        if m == '2':
            em = app_email.Email()
            msg = app_email.Message()

            msg.set_receiver("to@smtp.mailtrap.io")
            em.set_address("from@smtp.mailtrap.io")
            em.set_smtp_server("smtp.mailtrap.io")
            em.set_port(2525)
            em.set_username("c123d2a294f857")
            em.set_password("07dc82c500f623")
            em.set_email_name('A user')
            
            message = f"""\
Subject: Test Email
To: {msg.receiver}
From: {em.email_name} <{em.address}>
                
{msg_1}"""
            
            msg.send_text_email(em, message)
            print("Email Sent")
        if m == '3':
            sms = phone_pc.PcPhone()
            sms.set_username('a_username')
            sms.set_account_sid('ACa00701c3867a69f3eef76f84bc7ddd5a')
            sms.set_auth_token('64e14618a92ef536a354b97be1381986')
            sms.set_recip('+18327386625')
            sms.set_sender('+12066811505')
            #sms.set_twml("https://rey242.github.io/test.xml")
            sms.set_voice_message(f'<Response><Say>{msg_1}</Say></Response>')
            suc,sid = sms.call_recip()
            print(suc + ' - Phone')


        

def app_address_book():
    with open('app_address_book.pkl', 'rb') as out:
        ab = pickle.load(out)
    return ab


def main():
    msg_choice = None
    recip_choice = None
    book = app_address_book()
    msg = None
    while True:
        choice = main_menu()
        if choice == '1':
            msg_choice = messaging_options()
        if choice == '2':
            recip_choice = recip_select(book)
        if choice == '3':
            msg = enter_message()
        if choice == '4':
            send_messages(msg_choice, msg)
        if choice == '5':
            settings()
        if choice == '6':
            access_address_book(book)
        if choice == '7':
            return

if __name__ == '__main__':
    main()