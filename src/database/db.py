from ZODB import FileStorage, DB
import transaction
from persistent import Persistent
from persistent.list import PersistentList
import BTrees.OOBTree

from All_class.Admin import Admin
from All_class.Doctor import Doctor

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

def printInfo():
    print("user id count: ", root.user_id_count)
    print("employee id list: ", root.employee_id_list)
    for user in root.users.values():
        print(user.get_id(), user.__class__.__name__ ,user.fname, user.password)
        # if user.role == "Doctor":
        #     print(type(user.salary))

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

def add_admin_if_no_admin():
    if len(root.employee_id_list) == 0:
        add_admin()

def add_doctor_if_no_doctor():
    if not any(isinstance(user, Doctor) for user in root.users.values()):
        print("Adding 3 doctors")
        add_doctor("Doctor1")
        add_doctor("Doctor2")
        add_doctor("Doctor3")

def addAdminAndDoctor():
    add_admin_if_no_admin()
    add_doctor_if_no_doctor() 