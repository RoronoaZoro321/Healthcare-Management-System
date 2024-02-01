import Person

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