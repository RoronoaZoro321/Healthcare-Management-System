from .Staff import Staff
from .Log import Log

class Admin(Staff):
    def __init__(self, fname: str, lname: str, address: str, phone_number: str, password: str ,employee_id: str, 
                    department: str, role: str, specialty: list[str], 
                    qualifications: str, salary: int):
        super().__init__(fname, lname,address, phone_number, password, employee_id, department, role)
        self.specialty = specialty
        self.qualifications = qualifications
        self.salary = salary
        
    def view_log(self):
        pass
    
    def view_doctor(self):
        pass
    
    def view_payment(self):
        pass
    
    # def add_doctor():
    #     doctor = Doctor("John", "Doe", "1234 Main St", "123-456-7890", "password", "123", "Cardiology", "Doctor", ["Heart"], "MD", 100000)
    #     root.user_id_count += 1
    #     root.users[root.user_id_count] = doctor
    #     transaction.commit()
    