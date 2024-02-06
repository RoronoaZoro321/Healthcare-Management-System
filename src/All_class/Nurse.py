from .Staff import Staff

class Nurse(Staff):
    def __init__(self, fname: str, lname: str, address: str, phone_number: str, password: str ,employee_id: str, 
                    department: str, role: str, assigned_wards: list[str], 
                    qualifications: str, salary: int):
        super().__init__(fname, lname,address, phone_number, password, employee_id, department, role)
        self.assigned_wards = assigned_wards
        self.qualifications = qualifications
        self.salary = salary
    
    def patient_care(self):
        pass
    
    def patient_report(self):
        pass
    