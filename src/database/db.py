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

def printInfo():
    print("user id count: ", root.user_id_count)
    print("employee id list: ", root.employee_id_list)
    for user in root.users.values():
        print(user.get_id(), user.__class__.__name__ ,user.fname, user.password)
        # if user.role == "Doctor":
        #     print(type(user.salary))
    print("log id count: ", root.log_id_count)

def add_doctor(name):
    root.user_id_count += 1
    doctor = Doctor(name, "lname", "123 Main St", "123-456-7890", "password", root.user_id_count, "Cardiology", "Doctor", ["Cardiology"], "MD", 80000)
    root.users[root.user_id_count] = doctor
    root.employee_id_list.append(root.user_id_count)
    transaction.commit()

def add_admin():
    root.user_id_count += 1
    admin = Admin("admin", "admin", "123 Main St", "123-456-7890", "password", root.user_id_count, "System Management", "Admin")
    root.users[root.user_id_count] = admin
    root.employee_id_list.append(root.user_id_count)
    transaction.commit()

def add_nurse(name):
    root.user_id_count += 1
    nurse = Nurse(name, "lname", "123 Main St", "123-456-7890", "password", root.user_id_count, "Cardiology", "Nurse", ["Cardiology"], "BD", 50000)
    root.users[root.user_id_count] = nurse
    root.employee_id_list.append(root.user_id_count)
    transaction.commit()

def add_patient(name):
    root.user_id_count += 1
    patient = Patient(name, "lname", "123 Main St", "123-456-7890", "password", root.user_id_count)
    root.users[root.user_id_count] = patient
    transaction.commit()


def add_admin_if_no_admin():
    if len(root.employee_id_list) == 0:
        add_admin()

def add_doctor_if_no_doctor():
    if not any(isinstance(user, Doctor) for user in root.users.values()):
        print("Adding 3 doctors")
        add_doctor("Doctor1")
        add_doctor("Doctor2")
        add_doctor("Doctor3")

def add_nurse_if_no_nurse():
    if not any(isinstance(user, Nurse) for user in root.users.values()):
        print("Adding 3 nurses")
        add_nurse("Nurse1")
        add_nurse("Nurse2")
        add_nurse("Nurse3")

def add_patient_if_no_patient():
    if not any(isinstance(user, Patient) for user in root.users.values()):
        print("Adding 3 patients")
        add_patient("Patient1")
        add_patient("Patient2")
        add_patient("Patient3")

def authenticate_user_db(username, password):
    for user in root.users.values():
        if user.get_fname() == username and user.get_password() == password:
            current_user = user
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


def addAdminAndDoctor():
    add_admin_if_no_admin()
    add_doctor_if_no_doctor() 
    add_nurse_if_no_nurse()
    add_patient_if_no_patient()


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
    print(actor.get_fname(), actor.get_lname())
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
