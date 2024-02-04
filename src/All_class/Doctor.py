from .Staff import Staff

class Doctor(Staff):
    def __init__(self, name: str, address: str, phone_number: str, employee_id: str, department: str, role: str, specialty: list[str], qualifications: str):
        super().__init__(name, address, phone_number, employee_id, department, role)
        self.specialty = specialty
        self.qualifications = qualifications
        
    def update_schedule(self):
        pass
    
    def select_nurse(self):
        pass
    
    def patient_report(self):
        pass

        