from .Person import Person
from abc import ABC, abstractmethod

class Staff(Person, ABC):
    def __init__(self, name: str, address: str, phone_number: str, employee_id: str, department: list[str], role: str):
        super().__init__(name, address, phone_number)
        self.employee_id = employee_id
        self.department = department
        self.role = role
        
    @abstractmethod
    def update_schedule(self):
        pass
    
    @abstractmethod
    def log_hours(self):
        pass
    
    @abstractmethod
    def patient_report(self):
        pass
    
    