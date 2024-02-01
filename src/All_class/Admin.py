import Staff
import Log

class Admin(Staff):
    def __init__(self, name: str, address: str, phone_number: str, employee_id: str, department: str, role: str):
        super().__init__(name, address, phone_number, employee_id, department, role)
        
    def view_log(self):
        pass
    
    def view_doctor(self):
        pass
    
    def view_payment(self):
        pass
    
    