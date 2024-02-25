from .Person import Person
from persistent.list import PersistentList
# from .db

class Patient(Person):
    def __init__(self, fname: str, lname: str, address: str, 
                 phone_number: str, password: str, patient_id: int,
                 photo=None, medical_history=None):
        super().__init__(fname=fname, lname=lname, address=address, 
                         phone_number=phone_number, password=password,
                         photo=photo)
        self.patient_id = patient_id
        self.medical_history = {}
        self.appointments = PersistentList()
    
    def get_id(self):
        return self.patient_id

    def schedule_appointment(self):
        pass

    def update_medical_history(self):
        pass

    def update_attributes(self, new_data):
        # ['John', 'Doe', '123 Main St', '123-456-7890', '12345']
        self.set_fname(new_data[0])
        self.set_lname(new_data[1])
        self.set_address(new_data[2])
        self.set_phone_number(new_data[3])
    
    # def add_appointment(self, appointment):
    #     self.appointments.append(appointment)
    #     self._p_changed = True
    #     trans

