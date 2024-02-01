import hashlib
import persistent
from persistent.list import PersistentList

class Person(persistent.Persistent):
    def __init__(self, fname: str, lname: str, address: str, 
                 phone_number: str, photo: str, password: str):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.phone_number = phone_number
        self.photo = photo
        self.password = password
    def update_detail(self, new_address: str, new_phone_number: str):
        self.phone_number = new_phone_number
        self.address = new_address
    
    def get_fname(self):
        return self.fname
    
    def get_lname(self):
        return self.lname
    
    def get_address(self):
        return self.address
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_photo(self):
        return self.photo
    
    def get_password(self):
        return self.password    

    def get_detail(self):
        return self.fname, self.lname, self.address, self.phone_number







    
        