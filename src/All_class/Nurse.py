from .Staff import Staff

class Nurse(Staff):
    def __init__(self, name: str, address: str, phone_number: str, employee_id: str, department: str, role: str, assigned_wards: list[str], qualifications: str):
        super().__init__(name, address, phone_number, employee_id, department, role)
        self.assigned_wards = assigned_wards
        self.qualifications = qualifications
    
    def patient_care(self):
        pass
    
    def patient_report(self):
        pass
    