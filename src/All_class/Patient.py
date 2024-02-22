from .Person import Person

class Patient(Person):
    def __init__(self, fname: str, lname: str, address: str, 
                 phone_number: str, password: str, patient_id: int,
                 photo=None, medical_history=None):
        super().__init__(fname=fname, lname=lname, address=address, 
                         phone_number=phone_number, password=password,
                         photo=photo)
        self.patient_id = patient_id
        self.medical_history = {}
    
    def get_id(self):
        return self.patient_id
    
    def schedule_appointment(self):
        pass

    def update_medical_history(self):
        pass