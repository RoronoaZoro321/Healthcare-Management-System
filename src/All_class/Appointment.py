class Appointment:
    def __init__(self, id, patient, doctor, nurse, confirm, start_time, end_time):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.nurse = nurse
        self.confirm = confirm
        self.start_time = start_time
        self.end_time = end_time
        
    def cancle(self):
        pass
    
    def schedule(self):
        pass