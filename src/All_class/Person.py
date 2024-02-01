import hashlib

class Person:
    def __init__(self, fname: str, lname: str, address: str, 
                 phone_number: str, photo: str, password: str):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.phone_number = phone_number
        self.photo = photo
        self.password = password

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

class Patient(Person):
    def __init__(self, fname: str, lname: str, address: str, 
                 phone_number: str, photo: str, password: str, 
                 patient_id: int, medical_history: str):
        super().__init__(fname, lname, address, phone_number, photo, password)
        self.patient_id = patient_id
        self.medical_history = {}

    def schedule_appointment(self):
        pass

    def update_medical_history(self):
        pass


