from .Staff import Staff
from persistent.list import PersistentList

class Doctor(Staff):
    def __init__(self, fname: str, lname: str, address: str, phone_number: str, password: str ,employee_id: str, 
                 department: str, role: str, specialty: list[str], 
                 qualifications: str, salary: int, working_time: str):
        super().__init__(fname, lname,address, phone_number, password, employee_id, department, role)
        self.specialty = specialty
        self.qualifications = qualifications
        self.salary = salary
        self.working_time = working_time #"8:00-17:00"
        self.appointments = PersistentList()
    
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
    
    def set_working_time(self, working_time):
        self.working_time = working_time
    
    def get_working_time(self):
        return self.working_time

    def add_appointment(self, appointment_id):
        self.appointments.append(appointment_id)
        self._p_changed = True

    def remove_appointment(self, appointment_id):
        if appointment_id in self.appointments:
            self.appointments.remove(appointment_id)
            self._p_changed = True
            
    def get_appointments(self):
        return list(self.appointments)

    def update_attributes(self, new_data):
        # ['doctor1', 'lname', '123 Main St', '123-456-7890', 'Cardiology', 'MDu', '80000', '8:00-17:00']
        super().update_attributes(new_data[0], new_data[1], new_data[2], new_data[3])
        self.set_specialty(new_data[4])
        self.set_qualifications(new_data[5])
        self.set_salary(int(new_data[6]))
        self.set_working_time(new_data[7])
    
    def update_schedule(self):
        pass
    
    def select_nurse(self):
        pass
    
    def patient_report(self):
        pass
