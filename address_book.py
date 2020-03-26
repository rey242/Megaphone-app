import re

class Contact:
    def __init__(self):
        self.name = None
        self.email = None
        self.cell_phone = None
        self.home_phone = None
        self.office_phone = None

    def set_name(self,name):
        self.name = name
    
    def set_email(self,email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        else:
            self.email = email
            return True
    
    def set_cell_phone(self,cp):
        cp = re.sub('\D', '', str(cp))
        if cp == '':
            self.cell_phone = cp
            return True
        if len(cp) != 10:
            return False
        self.cell_phone = cp
        return True

    def set_home_phone(self,hp):
        hp = re.sub('\D', '', str(hp))
        if hp == '':
            self.home_phone = hp
            return True
        if len(hp) != 10:
            return False
        self.home_phone = hp
        return True
    
    def set_office_phone(self,op):
        op = re.sub('\D', '', str(op))
        if op == '':
            self.office_phone = op
            return True
        if len(op) != 10:
            return False
        self.office_phone = op
        return True

class AddressBook:
    def __init__(self):
        self.book = {}

    def add_entry(self,name):
        if name is '' or type(name) != str or name in self.book.keys():
            return False
        new = Contact()
        new.set_name(name)
        self.book[name] = new
        return True

    def get_entry(self,name):
        if name in self.book:
            return self.book[name]
        else:
            return False
    
    def list_of_entries(self):
        t = []
        for x in self.book:
            t.append(x)
        return t

    def delete_entry(self,name):
        del self.book[name]
    