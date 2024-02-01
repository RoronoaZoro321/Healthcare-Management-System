class Person:
    def __init__(self,fname,lname,address, phone_number):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.phone_number = phone_number

    def get_detail(self):
        pass

class Patient(Person):
    def __init__(self, fname, lname, address, phone_number,patient_id,medical_history):
        super().__init__(fname, lname, address, phone_number)
        self.patient_id = patient_id
        self.update_medical_history = medical_history
    def schedule_appointment(self):
        pass

    def update_medical_history(self):
        pass




    
        