from ZODB import FileStorage, DB
import transaction
from persistent import Persistent
from persistent.list import PersistentList
import BTrees.OOBTree

from All_class.Admin import Admin
from All_class.Doctor import Doctor
from All_class.Patient import Patient
from All_class.Nurse import Nurse
from All_class.Log import Log
from All_class.Appointment import Appointment
from All_class.Report import Medicine, Service, Bill, MedicalRecord, Report

storage = FileStorage.FileStorage('src/database/healthcare_management.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

current_user = None

print("database opened")

def initialize_database():
    print("has attr users: ", hasattr(root, "users"))
    if not hasattr(root, "users"):
        root.users = BTrees.OOBTree.BTree()

    print("user id count: ", hasattr(root, "user_id_count"))
    if not hasattr(root, "user_id_count"):
        root.user_id_count = 0

    print("employee id list: ", hasattr(root, "employee_id_list"))
    if not hasattr(root, "employee_id_list"):
        root.employee_id_list = PersistentList()

    print("has attr logs: ", hasattr(root, "logs"))
    if not hasattr(root, "logs"):
        root.logs = BTrees.OOBTree.BTree()

    print("has attr log id count: ", hasattr(root, "log_id_count"))
    if not hasattr(root, "log_id_count"):
        root.log_id_count = 0
    
    print("has attr appointment", hasattr(root, "appointments"))
    if not hasattr(root, 'appointments'):
        root.appointments = BTrees.OOBTree.BTree()

    print("appointment id count", hasattr(root, "last_appointment_id"))
    if not hasattr(root, 'last_appointment_id'):
        root.last_appointment_id = 0 
        
    print("appointment id list: ", hasattr(root, "appointment_id_list"))
    if not hasattr(root, "appointment_id_list"):
        root.appointment_id_list = PersistentList()
    
    print("has attr reports: ", hasattr(root, "reports"))
    if not hasattr(root, "reports"):
        root.reports = BTrees.OOBTree.BTree()
    
    print("report id count: ", hasattr(root, "report_id_count"))
    if not hasattr(root, "report_id_count"):
        root.report_id_count = 0
    
    print("has attr medicines: ", hasattr(root, "medicines"))
    if not hasattr(root, "medicines"):
        root.medicines = BTrees.OOBTree.BTree()
    
    print("has attr current_medicine_selected: ", hasattr(root, "current_medicine_selected"))
    if not hasattr(root, "current_medicine_selected"):
        root.current_medicine_selected = PersistentList()
    
    print("has attr current_service_selected: ", hasattr(root, "current_service_selected"))
    if not hasattr(root, "current_service_selected"):
        root.current_service_selected = PersistentList()
    
    root.current_medicine_selected = []
    root.current_service_selected = []

def printInfo():
    print("user id count: ", root.user_id_count)
    print("employee id list: ", root.employee_id_list)
    for user in root.users.values():
        print(user.get_id(), user.__class__.__name__ ,user.fname, user.password)
        # if user.role == "Doctor":
        #     print(type(user.salary))
    print("log id count: ", root.log_id_count)
    print("reports id count: ", root.report_id_count)

def print_appointment_info():
    for appointment_id, appointment in root.appointments.items():
        print(f"Appointment ID: {appointment_id}")
        print(f"Date: {appointment.date}")
        print(f"Start Time: {appointment.start_time}")
        print(f"End Time: {appointment.end_time}")
        print(f"Doctor ID: {appointment.doctor}")
        if appointment.doctor in root.users:
            doctor = root.users[appointment.doctor]
            print(f"Doctor Name: {doctor.fname} {doctor.lname}")
        else:
            print("Doctor ID not found in users")
        print(f"Confirmation: {appointment.confirm}")
        print(f"Patient ID: {appointment.patient} \n")
        
def delete_all_appointments():
    appointment_ids = list(root.appointments.keys())
    for appointment_id in appointment_ids:
        del root.appointments[appointment_id]
    transaction.commit()

    root.last_appointment_id = 0
    root.appointment_id_list = PersistentList()
    transaction.commit()


def add_first_admin():
    root.user_id_count += 1
    admin = Admin("admin", "Admin1", "Admin1", "Admin1", "password", root.user_id_count, "Main Head", "Admin")
    root.users[root.user_id_count] = admin
    root.employee_id_list.append(root.user_id_count)
    transaction.commit()

def add_doctor(current_user, fname, lname, address, phone_number, password, department, specialty, degree, salary, working_time):
    root.user_id_count += 1
    specialty = specialty.split(",")
    doctor = Doctor(fname, lname, address, phone_number, password, root.user_id_count, department, "Doctor", specialty, degree, salary, working_time)
    root.users[root.user_id_count] = doctor
    root.employee_id_list.append(root.user_id_count)
    add_log_db(current_user, "added Doctor", doctor)
    transaction.commit()

def add_admin(current_user, fname, lname, address, phone_number, password, department):
    root.user_id_count += 1
    admin = Admin(fname, lname, address, phone_number, password, root.user_id_count, department, "Admin")
    root.users[root.user_id_count] = admin
    root.employee_id_list.append(root.user_id_count)
    add_log_db(current_user, "added Admin", admin)
    transaction.commit()

def add_nurse(current_user, fname, lname, address, phone_number, password, department, assigned_wards, qualifications, salary, working_time):
    root.user_id_count += 1
    assigned_wards = assigned_wards.split(",")
    nurse = Nurse(fname, lname, address, phone_number, password, root.user_id_count, department, "Nurse", assigned_wards, qualifications, salary, working_time)
    root.users[root.user_id_count] = nurse
    root.employee_id_list.append(root.user_id_count)
    add_log_db(current_user, "added Nurse", nurse)
    transaction.commit()

def add_patient(current_user, fname, lname, address, phone_number, password):
    root.user_id_count += 1
    patient = Patient(fname, lname, address, phone_number, password, root.user_id_count)
    root.users[root.user_id_count] = patient
    add_log_db(current_user, "added Patient", patient)
    transaction.commit()

def add_admin_if_no_admin():
    if len(root.employee_id_list) == 0:
        add_first_admin()

def add_doctor_if_no_doctor():
    if not any(isinstance(user, Doctor) for user in root.users.values()):
        print("Adding 3 doctors")
        add_doctor(root.users[1],"doctor1", "doe", "123 street", "1234567890", "password", "Surgery", "Heart,Brain", "MD", 100000, "8:00-17:00")
        add_doctor(root.users[1],"doctor2", "doe", "123 street", "1234567890", "password", "Surgery", "Face", "DD", 290000, "10:00-19:00")
        add_doctor(root.users[1],"doctor3", "doe", "123 street", "1234567890", "password", "Orthopedics", "Bone", "MD", 150000, "12:00-21:00")

def add_nurse_if_no_nurse():
    if not any(isinstance(user, Nurse) for user in root.users.values()):
        print("Adding 3 nurses")
        add_nurse(root.users[1],"nurse1", "doe", "123 street", "1234567890", "password", "Cardiology", "1,2,3", "BSc", 50000, "8:00-17:00")
        add_nurse(root.users[1],"nurse2", "doe", "123 street", "1234567890", "password", "Neurology", "4,5,6", "BSc", 50000, "11:00-20:00")
        add_nurse(root.users[1],"nurse3", "doe", "123 street", "1234567890", "password", "Orthopedics", "7,8,9", "BSc", 50000, "8:00-24:00")

def add_patient_if_no_patient():
    if not any(isinstance(user, Patient) for user in root.users.values()):
        print("Adding 3 patients")
        add_patient(root.users[1],"p1", "doe", "123 street", "1234567890", "password")
        add_patient(root.users[1],"patient2", "doe", "123 street", "1234567890", "password")
        add_patient(root.users[1],"patient3", "doe", "123 street", "1234567890", "password")
    
def add_medicine_if_no_medicine():
    if not any(isinstance(medicine, Medicine) for medicine in root.medicines.values()):
        print("Adding 6 medicines")
        add_medicine_db("u4083", "Parazetamol", "For fever", 100, "2 weeks", "after breakfast", 10)
        add_medicine_db("gg083", "Sara", "For headache", 200, "1 week", "before sleep", 20)
        add_medicine_db("ki083", "Serphony", "For cold", 300, "3 days", "2 capsule before dinner", 30)
        add_medicine_db("lo083", "Tyraxynl", "For cough", 400, "1 week", "after breakfast", 40)
        add_medicine_db("pou03", "Polymorzync", "For stomach pain", 500, "2 weeks", "when have fever", 50)
        add_medicine_db("uu083", "Gyhofrewoqy", "For body pain", 600, "1 week", "3 capsule before dinner", 60)

def add_report_if_no_report():
    if not any(isinstance(report, Report) for report in root.reports.values()):
        print("Adding 2 reports to patient 1 and 1 report to patient 2")
        patient1 = get_patient_by_name("p1")
        patient2 = get_patient_by_name("patient2")
        
        medical_record = MedicalRecord(180, 80, "male", 80, 120, "none", "Headage", "Having High Headage pain", "lorem ipsum dolor sit amet consectetuer adipiscing elit")
        bill = Bill(0.1)
        service_1 = Service("Checking", 100, 0.1, "Thai Care", 50)
        service_2 = Service("X-ray", 100, 0.1, "Thai Care", 50)
        medicine_1 = Medicine("u4083", "Parazetamol", "For fever", 100, "2 weeks", "after breakfast", 10)
        medicine_2 = Medicine("gg083", "Sara", "For headache", 200, "1 week", "before sleep", 20)
        bill.setServices([service_1, service_2])
        bill.setMedicines([medicine_1, medicine_2])
        add_report(patient1.get_id(), root.users[2], medical_record, bill)
        add_report(patient2.get_id(), root.users[2], medical_record, bill)
        bill.setServices([service_1])
        bill.setMedicines([medicine_1])    
        add_report(patient1.get_id(), root.users[2], medical_record, bill)

def authenticate_user_db(username, password):
    for user in root.users.values():
        if user.get_fname() == username:
            if user.verify_password(password):
                current_user = user
                add_log_db(current_user, "logged in", current_user)
                return current_user
    return None

def register_user_db(fname, lname, address, phone_number, password):
    for i in root.users:
        if root.users[i].get_fname() == fname:
            return False
    root.user_id_count += 1
    patient = Patient(fname, lname, address, phone_number, password, root.user_id_count)
    root.users[root.user_id_count] = patient
    transaction.commit()
    current_user = patient
    return current_user


def addUsersAndOthers():
    add_admin_if_no_admin()
    add_doctor_if_no_doctor() 
    add_nurse_if_no_nurse()
    add_patient_if_no_patient()
    add_medicine_if_no_medicine()
    add_report_if_no_report()


def delete_user_db(user_id):
    del root.users[user_id]
    transaction.commit()

def delete_user_db_by_id(current_user, user_id):
    if user_id in root.users:
        if isinstance(root.users[user_id], Admin):
            print("Cannot delete admin")
            return False
        elif isinstance(root.users[user_id], Doctor):
            add_log_db(current_user, "deleted Doctor", root.users[user_id])
            del root.users[user_id]
            root.employee_id_list.remove(user_id)
            root.employee_id_list._p_changed = True
            transaction.commit()
            # print("Deleted Doctor ", user_id)
            return True
        elif isinstance(root.users[user_id], Nurse):
            add_log_db(current_user, "deleted Nurse", root.users[user_id])
            del root.users[user_id]
            root.employee_id_list.remove(user_id)
            root.employee_id_list._p_changed = True
            transaction.commit()
            # print("Deleted Nurse ", user_id)
            return True
        elif isinstance(root.users[user_id], Patient):
            add_log_db(current_user, "deleted Patient", root.users[user_id])
            del root.users[user_id]
            transaction.commit()
            # print("Deleted Patient ", user_id)
            return True
    return False

def getUserToDisplay(role, search_text, search_attribute):
    users_to_display = []

    if role == "Doctor" or role == "Nurse":
        for i in root.employee_id_list:
            if root.users[i].role == role and search_text in str(getattr(root.users[i], search_attribute)).lower():
                users_to_display.append(root.users[i])
    else:
        for i in root.users:
            if root.users[i].__class__.__name__ == role:
                if search_text in str(getattr(root.users[i], search_attribute)).lower():
                    users_to_display.append(root.users[i])
    
    return users_to_display

def update_user_attributes(current_user, user_id, data):
    root.users[user_id].update_attributes(data)  # Assuming a method to update attributes
    add_log_db(current_user, "updated data for", root.users[user_id])
    transaction.commit()

def add_log_db(actor, action, target):
    root.log_id_count += 1
    log = Log(root.log_id_count, actor, action, target)
    root.logs[root.log_id_count] = log
    transaction.commit()

def get_logs():
    logs = []
    for i in root.logs:
        logs.append(root.logs[i])
    return logs

def delete_log_db():
    for i in root.logs:
        del root.logs[i]
    root.log_id_count = 0
    transaction.commit()

def get_all_patients():
    patients = []
    for i in root.users:
        if root.users[i].__class__.__name__ == "Patient":
            patients.append(root.users[i])
    return patients

def get_patient_by_id(patient_id):
    return root.users[patient_id]

def get_patient_by_name(name):
    for i in root.users:
        if root.users[i].__class__.__name__ == "Patient":
            if root.users[i].get_fname() == name:
                return root.users[i]
    return None

def get_all_staffs():
    staffs = []
    for i in root.employee_id_list:
        staffs.append(root.users[i])
    return staffs

def get_all_doctor_and_nurse():
    staffs = []
    for i in root.employee_id_list:
        if root.users[i].__class__.__name__ == "Doctor" or root.users[i].__class__.__name__ == "Nurse":
            staffs.append(root.users[i])
    return staffs

def add_medicine_db(medicine_id, name, description, quantity, duration, when, price_per_dose):
    medicine = Medicine(medicine_id ,name, description, int(quantity), duration, when, int(price_per_dose))
    root.medicines[medicine_id] = medicine
    transaction.commit()
    return medicine

def search_medicine_db(text):
    medicines = []
    for i in root.medicines:
        if text.lower() in root.medicines[i].name.lower():
            medicines.append(root.medicines[i])
    return medicines

def get_medicine(medicine_id):
    return root.medicines[medicine_id]

def save_list_of_medicine(medicine_list):
    root.current_medicine_selected = medicine_list
    transaction.commit()

def get_list_of_medicine():
    return root.current_medicine_selected

def add_service_db(name, price, discount_percentage, insurance_name, insurance_coverage):
    service = Service(name, float(price), float(discount_percentage), insurance_name, float(insurance_coverage))
    transaction.commit()
    return service

def save_service_list(service_list):
    root.current_service_selected = service_list
    transaction.commit()

def get_list_of_service():
    return root.current_service_selected

def createBill(overallDiscount):
    bill = Bill(float(overallDiscount))
    bill.setServices(root.current_service_selected)
    bill.setMedicines(root.current_medicine_selected)
    transaction.commit()
    return bill

def createMedicalRecord(height, weight, sex, pulse_rate, blood_pressure, allegies, title, description, details):
    medical_record = MedicalRecord(float(height), float(weight), sex, float(pulse_rate), float(blood_pressure), allegies, title, description, details)
    transaction.commit()
    return medical_record

def add_report(patient_id, current_user, medical_record, bill):
    root.report_id_count += 1
    report = Report(root.report_id_count, patient_id, current_user.get_id(), medical_record, bill)
    root.reports[root.report_id_count] = report
    # add report to patient
    patient = root.users[patient_id]
    patient.add_medical_history(report)
    transaction.commit()
    return report

def get_all_reports():
    reports = []
    for i in root.reports:
        reports.append(root.reports[i])
    return reports