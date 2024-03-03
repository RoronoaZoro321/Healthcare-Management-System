import persistent
from persistent.list import PersistentList

class Person(persistent.Persistent):
    def __init__(self, fname: str, lname: str, address: str, 
                 phone_number: str,password: str, photo: str = None):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.phone_number = phone_number
        self.photo = photo
        self.password = password
    
    def update_attributes(self, fname: str, lname: str, address: str, phone_number: str):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.phone_number = phone_number
    
    def get_fname(self):
        return self.fname
    
    def get_lname(self):
        return self.lname
    
    def get_address(self):
        return self.address
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_photo(self):
        return self.photo
    
    def get_password(self):
        return self.password    

    def get_detail(self):
        return self.fname, self.lname, self.address, self.phone_number
    
    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname
    
    def set_address(self, address):
        self.address = address
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def set_photo(self, photo):
        self.photo = photo
    
    def set_password(self, password):
        self.password = password

class Patient(Person):
    def __init__(self, fname: str, lname: str, address: str, 
                 phone_number: str, password: str, patient_id: int,
                 photo=None, medical_history=None):
        super().__init__(fname=fname, lname=lname, address=address, 
                         phone_number=phone_number, password=password,
                         photo=photo)
        self.patient_id = patient_id
        self.medical_history = {}
        self.appointments = PersistentList()
    
    def get_id(self):
        return self.patient_id

    def schedule_appointment(self):
        pass

    def update_medical_history(self):
        pass

    def update_attributes(self, new_data):
        # ['John', 'Doe', '123 Main St', '123-456-7890', '12345']
        super().update_attributes(new_data[0], new_data[1], new_data[2], new_data[3])
    
    def add_appointment(self, id):
        self.appointments.append(id)
        self._p_changed = True

from abc import ABC, abstractmethod

class Staff(Person, ABC):
    def __init__(self, fname: str, lname:str, address: str, phone_number: str, password: str, employee_id: int, department: list[str], role: str):
        super().__init__(fname, lname, address, phone_number, password)
        self.employee_id = employee_id
        self.department = department
        self.role = role

    def get_id(self):
        return self.employee_id
    
    def get_department(self):
        return self.department
    
    def get_role(self):
        return self.role
    
    def set_id(self, id):
        self.employee_id = id

    def set_department(self, department):
        self.department = department
    
    def set_role(self, role):
        self.role = role        
        
    @abstractmethod
    def update_schedule(self):
        pass
    
    @abstractmethod
    def log_hours(self):
        pass
    
    @abstractmethod
    def patient_report(self):
        pass
    
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

    def add_appointment(self, id):
        self.appointments.append(id)
        self._p_changed = True
    
    def get_appointments(self):
        return self.appointments

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
    
    def set_working_time(self, working_time):
        self.working_time = working_time
    
    def get_working_time(self):
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
        self.set_working_time(new_data[7])

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
    
    def create_doctor(self):
        pass

from datetime import datetime

class Log(persistent.Persistent):
    def __init__(self, id: int, actor, action: str, target):
        self.id = id
        self.time = datetime.now()
        self.actor = actor
        self.action = action
        self.target = target
    
    def get_id(self):
        return self.id
    
    def get_time(self):
        return self.time.strftime("%m/%d/%Y, %H:%M:%S")

    def get_actor(self):
        return self.actor    
    
    def get_action(self):
        return self.action
    
    def get_target(self):
        return self.target
    
    def get_details(self):
        return f"{self.id} {self.time} {self.actor.get_fname()} {self.action} {self.target.get_fname()}"
    
    def get_actor_fname(self):
        return self.actor.get_fname()
    
    def get_target_fname(self):
        return self.target.get_fname()

class Appointment(persistent.Persistent):
    def __init__(self, id, date, start_time, end_time, doctor, speciality, patient, confirm):
        self.id = id
        self.date = date
        self.patient = patient
        self.doctor = doctor
        self.speciality = speciality
        self.confirm = confirm
        self.start_time = start_time
        self.end_time = end_time
        self.room_number = None
        
    def cancle(self):
        pass
    
    def schedule(self):
        pass
