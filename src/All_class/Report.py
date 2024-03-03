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

class Medicine(persistent.Persistent):
    def __init__(self, id, name, description, quantity, duration, when, price_per_dose):
        self.medicine_id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.duration = duration
        self.when_to_consume = when
        self.price_per_dose = price_per_dose
        self.total_price = self.calculate_price()
    
    def calculate_price(self):
        self.total_price = self.price_per_dose * self.quantity
        return self.total_price
    
class Report(persistent.Persistent):
    def __init__(self, id: int, patient_id: int, doctor_id: int, data: Data):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.data = data
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.medicines = PersistentList()

