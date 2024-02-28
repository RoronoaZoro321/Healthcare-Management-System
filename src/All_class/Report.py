import persistent
from persistent.list import PersistentList
from datetime import datetime

class Data(persistent.Persistent):
    def __init__(self, height, weight, sex, pulse_rate, blood_pressure, allegies, title, description, details):
        self.height = height
        self.weight = weight
        self.sex = sex
        self.pulse_rate = pulse_rate
        self.blood_pressure = blood_pressure
        self.allegies = allegies
        self.title = title
        self.description = description
        self.details = details

class Report(persistent.Persistent):
    def __init__(self, patient_id: int, doctor_id: int, data: str):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.data = data
        self.date = datetime.now().strftime("%Y-%m-%d")
    

