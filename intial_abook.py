import address_book
import pickle

with open('app_address_book.pkl','wb') as f:
    a = address_book.AddressBook()
    pickle.dump(a,f,pickle.HIGHEST_PROTOCOL)  
