import persistent

class Appointment(persistent.Persistent):
    def __init__(self, id, date, start_time, end_time, doctor, patient, confirm):
        self.id = id
        self.date = date
        self.patient = patient
        self.doctor = doctor
        self.confirm = confirm
        self.start_time = start_time
        self.end_time = end_time
        self.room_number = None
        
    def cancle(self):
        pass
    
    def schedule(self):
        pass