import persistent
from persistent.list import PersistentList
from datetime import datetime
from abc import ABC, abstractmethod

class MedicalRecord(persistent.Persistent):
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


class BillableItem(ABC,persistent.Persistent):
    def __init__(self, name, price, discount_percentage):
        self.name = name
        self.price = price
        self.discount_percentage = discount_percentage
        self.total = 0

    @abstractmethod
    def calculate_sum(self) -> float:
        pass

class Medicine(BillableItem):
    def __init__(self, id, name, description, quantity, duration, when_to_consume, price_per_dose):
        super().__init__(name, price_per_dose * quantity, discount_percentage=0)
        self.medicine_id = id
        self.description = description
        self.quantity = quantity
        self.duration = duration
        self.when_to_consume = when_to_consume
        self.price_per_dose = price_per_dose
        self.total = self.calculate_sum()

    def calculate_sum(self):
        return self.price_per_dose * self.quantity

class Service(BillableItem):
    def __init__(self, name, price, discount_percentage, insurance_name, insurance_coverage):
        super().__init__(name, price, discount_percentage)
        self.insurance_name = insurance_name
        self.insurance_coverage = insurance_coverage
        self.total = self.calculate_sum()

    def calculate_sum(self):
        self.total = self.price - self.insurance_coverage
        self.total = self.total - (self.total * self.discount_percentage)
        return self.total


class Bill(persistent.Persistent):
    def __init__(self, discount_percentage):
        self.services = PersistentList()
        self.medicines = PersistentList()
        self.discount_percentage = discount_percentage
    
    def setServices(self, services):
        self.services = services
    
    def setMedicines(self, medicines):
        self.medicines = medicines
    
    def total_services(self):
        total = 0
        for service in self.services:
            total += service.total
        return total
    
    def total_medicines(self):
        total = 0
        for medicine in self.medicines:
            total += medicine.total
        return total
    
    def total_without_discount(self):
        print(self.total_services())
        print(self.total_medicines())
        return self.total_services() + self.total_medicines()
    
    def total_after_discount(self):
        return self.total_without_discount() - (self.total_without_discount() * self.discount_percentage)

class Report(persistent.Persistent):
    def __init__(self, id: int, patient_id: int, doctor_id: int, medical_record: MedicalRecord, bill: Bill):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medical_record = medical_record
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.bill = bill
    
    def generate_report(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Date: {self.date}")
        print(f"Height: {self.medical_record.height}")
        print(f"Weight: {self.medical_record.weight}")
        for service in self.bill.services:
            print(f"Service: {service.name}")
            print(f"Price: {service.price}")
            print(f"Discount: {service.discount_percentage}")
            print(f"Insurance: {service.insurance_name}")
            print(f"Insurance Coverage: {service.insurance_coverage}")
        for medicine in self.bill.medicines:
            print(f"Medicine: {medicine.name}")
            print(f"Price: {medicine.price}")
            print(f"Discount: {medicine.discount_percentage}")
            print(f"Quantity: {medicine.quantity}")
            print(f"Duration: {medicine.duration}")
            print(f"When to Consume: {medicine.when_to_consume}")
            print(f"Price per Dose: {medicine.price_per_dose}")
        print(f"Total Services: {self.bill.total_services()}")
        print(f"Total Medicines: {self.bill.total_medicines()}")
        print(f"Total without Discount: {self.bill.total_without_discount()}")
        print(f"Total after Discount: {self.bill.total_after_discount()}")
        print(f"Title: {self.medical_record.title}")
        print(f"Description: {self.medical_record.description}")
        print(f"Details: {self.medical_record.details}")




def Test():
    # from All_class import Patient, Doctor
    # patient = Patient(1, "John", "Doe", "address", "phone", "password")
    # doctor = Doctor(2, "John", "Doe", "address", "phone", "password", "department", "specialty", "degree", 10000, "working_time")
    medical_record = MedicalRecord(180, 80, "male", 80, 120, "none", "title", "description", "details")
    bill = Bill(0.1)
    service = Service("service", 100, 0.1, "insurance_name", 50)
    service2 = Service("service2", 100, 0.1, "insurance_name", 50)
    medicine = Medicine(1, "medicine", "description", 10, 5, "when_to_consume", 10)
    medicine2 = Medicine(2, "medicine2", "description", 10, 5, "when_to_consume", 10)
    bill.setServices([service, service2])
    bill.setMedicines([medicine, medicine2])
    report = Report(1, 1, 2, medical_record, bill)
    report.generate_report()

if __name__ == "__main__":
    Test()
