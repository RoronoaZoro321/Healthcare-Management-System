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
        super().update_attributes(new_data[0], new_data[1], new_data[2], new_data[3])

    def add_appointment(self, appointment_id):
        self.appointments.append(appointment_id)
        self._p_changed = True

    def remove_appointment(self, appointment_id):
        if appointment_id in self.appointments:
            self.appointments.remove(appointment_id)
            self._p_changed = True

    def get_appointments(self):
        return list(self.appointments)

    def display_reports(self):
        for report in self.medical_history:
            report.display_report()

