from .Staff import Staff

class Doctor(Staff):
    def __init__(self, fname: str, lname: str, address: str, phone_number: str, password: str ,employee_id: str, 
                 department: str, role: str, specialty: list[str], 
                 qualifications: str, salary: int):
        super().__init__(fname, lname,address, phone_number, password, employee_id, department, role)
        self.specialty = specialty
        self.qualifications = qualifications
        self.salary = salary
        
    def update_schedule(self):
        pass
    
    def select_nurse(self):
        pass
    
    def patient_report(self):
        pass

        