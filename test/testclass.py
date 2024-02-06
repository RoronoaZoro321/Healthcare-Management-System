import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.All_class.Person import Person
from src.All_class.Patient import Patient
from src.All_class.Staff import Staff
from src.All_class.Doctor import Doctor
from src.All_class.Nurse import Nurse
from src.All_class.Admin import Admin
from src.All_class.Appointment import Appointment

class TestClass:
    def test_person(self):
        p = Person("John", "Doe", "1234 Main St.", "123-456-7890", "password")
        assert p.get_detail() == ("John", "Doe", "1234 Main St.", "123-456-7890")
        assert p.update_detail("1234 Main St.", "123-456-7890") == True
        print("Person test passed")

    def test_patient(self):
        p = Patient("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1)
        assert p.patient_id == 1
        assert p.get_id() == 1
        assert p.fname == "John"
        assert p.get_detail() == ("John", "Doe", "1234 Main St.", "123-456-7890")
        print("Patient test passed")
    
    def test_staff(self):
        s = Staff("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role")
        # print(s.employee_id, type(s.employee_id))
        assert s.employee_id == 1234
        assert s.department == ["dept1", "dept2"]
        assert s.role == "role"
        assert s.fname == "John"
        assert s.get_detail() == ("John", "Doe", "1234 Main St.", "123-456-7890")
        print("Staff test passed")
    
    def test_doctor(self):
        d = Doctor("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role", 
                   ["specialty1", "specialty2"], "qualification", 100000)
        assert d.employee_id == 1234
        assert d.salary == 100000
        print("Doctor test passed")

    def test_nurse(self):
        n = Nurse("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role", 
                   ["specialty1", "specialty2"], "qualification", 100000)
        assert n.employee_id == 1234
        assert n.salary == 100000
        print("Nurse test passed")

    def test_admin(self):
        a = Admin("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role", 
                   ["specialty1", "specialty2"], "qualification", 100000)
        assert a.employee_id == 1234
        assert a.salary == 100000
        print("Admin test passed")
    
    def test_appointment(self):
        p = Patient("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1)
        d = Doctor("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role", 
           ["specialty1", "specialty2"], "qualification", 100000)
        n = Nurse("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role", 
           ["specialty1", "specialty2"], "qualification", 100000)
        a = Appointment(id=1,patient=p,doctor=d,nurse=n,confirm=False,start_time="2021-10-10 10:00",end_time="2021-10-10 11:00")

        assert a.id == 1
        assert a.patient == p
        assert a.doctor == d
        assert a.nurse == n
        assert a.confirm == False
        assert a.start_time == "2021-10-10 10:00"
        assert a.end_time == "2021-10-10 11:00"
        print("Appointment test passed")

if __name__ == "__main__":
    tc = TestClass()
    tc.test_person()
    tc.test_patient()
    tc.test_staff()
    tc.test_doctor()
    tc.test_nurse()
    tc.test_admin()
    tc.test_appointment()
    from datetime import datetime
    print(datetime.now())
    print("Everything passed")  