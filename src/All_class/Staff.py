from .Person import Person
from abc import ABC, abstractmethod

class Staff(Person, ABC):
    def __init__(self, fname: str, lname:str, address: str, phone_number: str, password: str, employee_id: int, department: list[str], role: str):
        super().__init__(fname, lname, address, phone_number, password)
        self.employee_id = employee_id
        self.department = department
        self.role = role

    def get_id(self):
        return self.employee_id
    
    def get_department(self):
        return self.department
    
    def get_role(self):
        return self.role
    
    def set_id(self, id):
        self.employee_id = id

    def set_department(self, department):
        self.department = department
    
    def set_role(self, role):
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
    
    