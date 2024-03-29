from .Staff import Staff

class Doctor(Staff):
    def __init__(self, fname: str, lname: str, address: str, phone_number: str, password: str ,employee_id: str, 
                 department: str, role: str, specialty: list[str], 
                 qualifications: str, salary: int):
        super().__init__(fname, lname,address, phone_number, password, employee_id, department, role)
        self.specialty = specialty
        self.qualifications = qualifications
        self.salary = salary
    
    def get_specialty(self):
        return self.specialty
    
    def get_qualifications(self):
        return self.qualifications
    
    def get_salary(self):
        return self.salary

    def set_specialty(self, specialty):
        self.specialty = specialty
    
    def set_qualifications(self, qualifications):
        self.qualifications = qualifications

    def set_salary(self, salary):
        self.salary = salary

    def update_attributes(self, new_data):
        # ['doctor1', 'lname', '123 Main St', '123-456-7890', 'Cardiology', 'MDu', '80000']
        self.set_fname(new_data[0])
        self.set_lname(new_data[1])
        self.set_address(new_data[2])
        self.set_phone_number(new_data[3])
        self.set_department(new_data[4])
        self.set_qualifications(new_data[5])
        self.set_salary(int(new_data[6]))
    
    def update_schedule(self):
        pass
    
    def select_nurse(self):
        pass
    
    def patient_report(self):
        pass
