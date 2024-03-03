import sys
from PySide6.QtWidgets import QApplication
from database.db import initialize_database, addAdminAndDoctor, printInfo, delete_all_appointments, print_appointment_info, print_all_doctor_appointments, print_all_patient_appointments, clear_all_appointments
from window.LoginUI import LoginUI

if __name__ == "__main__":
    initialize_database()
    addAdminAndDoctor()
    printInfo()
    print_appointment_info()
    print_all_doctor_appointments()
    print_all_patient_appointments()
    app = QApplication(sys.argv)
    window = LoginUI()
    window.show()

    sys.exit(app.exec())


# if __name__ == "__main__":
#     initialize_database()
#     addAdminAndDoctor()
#     printInfo()

#     app = QApplication(sys.argv)
#     window = LoginUI()
#     window.show()

#     sys.exit(app.exec())
