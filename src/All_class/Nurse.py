from .Staff import Staff
from persistent.list import PersistentList

class Nurse(Staff):
    def __init__(self, fname: str, lname: str, address: str, phone_number: str, password: str ,employee_id: str, 
                    department: str, role: str, assigned_wards: list[str], 
                    qualifications: str, salary: int, working_time: str):
        super().__init__(fname, lname,address, phone_number, password, employee_id, department, role)
        self.assigned_wards = assigned_wards
        self.qualifications = qualifications
        self.salary = salary
        self.working_time = working_time # "8:00-17:00"
        self.appointments = PersistentList()
    
    def patient_care(self):
        pass
    
    def patient_report(self):
        pass

    def set_qualifications(self, qualifications):
        self.qualifications = qualifications
    
    def get_qualifications(self):
        return self.qualifications
    
    def set_salary(self, salary):
        self.salary = salary
    
    def get_salary(self):
        return self.salary
    
    def set_woking_time(self, working_time):
        self.working_time = working_time
    
    def get_woking_time(self):
        return self.working_time
    
    def add_appointment(self, id):
        self.appointments.append(id)
        self._p_changed = True
    
    def get_appointments(self):
        return self.appointments
    
    def update_attributes(self, new_data):
        # ['Nurse1', 'lname', '123 Main St', '123-456-7890', 'Cardiology', 'BD', '40000']
        super().update_attributes(new_data[0], new_data[1], new_data[2], new_data[3])
        self.set_department(new_data[4])
        self.set_qualifications(new_data[5])
        self.set_salary(int(new_data[6]))
        