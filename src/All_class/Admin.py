from .Staff import Staff
from .Log import Log

class Admin(Staff):
    def __init__(self, fname: str, lname: str, address: str, phone_number: str, password: str ,employee_id: str, 
                    department: str, role: str):
        super().__init__(fname, lname,address, phone_number, password, employee_id, department, role)
    
    def get_id(self):
        return self.employee_id

    def view_log(self):
        pass
    
    def view_doctor(self):
        pass
    
    def view_payment(self):
        pass
    