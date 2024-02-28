import hashlib
import persistent
from persistent.list import PersistentList
from abc import ABC, abstractmethod

class Person(persistent.Persistent, ABC):
    def __init__(self, fname: str, lname: str, address: str, 
                 phone_number: str,password: str, photo: str = None):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.phone_number = phone_number
        self.photo = photo
        self.password = self.hash(password)
    
    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def view_appintments(self):
        pass
    
    def update_attributes(self, fname: str, lname: str, address: str, phone_number: str):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.phone_number = phone_number
    
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
    
    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname
    
    def set_address(self, address):
        self.address = address
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def set_photo(self, photo):
        self.photo = photo
    
    def set_password(self, password):
        self.password = self.hash(password)
    
    def hash(self, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return hashed
    
    def verify_password(self, password):
        return self.password == self.hash(password)

