from PySide6.QtWidgets import *
from database.db import current_user

class AppController:
    def __init__(self):
        self.app = QApplication([])
        self.login_ui = None
        self.signup_ui = None
        self.main_window_ui = None
        self.main_window_admin_ui = None
        self.add_user_ui = None

    def start(self):
        self.show_login()

    def show_login(self):
        from window.LoginUI import LoginUI
        self.login_ui = LoginUI()
        self.login_ui.ui.pushButton.clicked.connect(self.authenticate_user)
        self.login_ui.ui.pushButton_2.clicked.connect(self.show_signup)
        self.login_ui.show()

    def show_signup(self):
        from window.SignupUI import SignupUI
        self.signup_ui = SignupUI()
        self.signup_ui.ui.pushButton_2.clicked.connect(self.show_login)
        self.signup_ui.ui.pushButton.clicked.connect(self.register_user)
        self.signup_ui.show()
        self.login_ui.hide()

    def authenticate_user(self, username, password):
        from database.db import authenticate_user_db
        if authenticate_user_db(username, password):
            self.show_main_window()
        else:
            QMessageBox.warning(self.login_ui, "Authentication Failed", "Invalid username or password.")

    def register_user(self,fname, lname, address, phone_number, password):
        from database.db import register_user_db
        current_user = register_user_db(fname, lname, address, phone_number, password)
        if not current_user:
            QMessageBox.warning(self.signup_ui, "Signup Failed", "User already exists")
        else:
            self.show_main_window()        

    def show_main_window(self):
        if current_user and current_user.__class__.__name__ == "Admin":
            self.show_main_window_admin()
        else:
            self.show_main_window_user()

    def show_main_window_admin(self):
        from window.MainWindowAdminUI import MainWindowAdminUI
        self.main_window_admin_ui = MainWindowAdminUI()
        self.main_window_admin_ui.ui.pushButton_4.clicked.connect(self.show_add_user)
        self.main_window_admin_ui.ui.pushButton_2.clicked.connect(self.show_profile_page)
        self.main_window_admin_ui.ui.pushButton_3.clicked.connect(self.show_appointment_page)
        self.main_window_admin_ui.ui.pushButton.clicked.connect(self.show_log_page)
        self.main_window_admin_ui.ui.pushButton_5.clicked.connect(self.show_list_doctor_page)
        self.main_window_admin_ui.ui.pushButton_6.clicked.connect(self.show_list_nurse_page)
        self.main_window_admin_ui.ui.pushButton_7.clicked.connect(self.show_list_patient_page)
        self.main_window_admin_ui.ui.pushButton_8.clicked.connect(self.show_add_user)
        self.main_window_admin_ui.ui.pushButton_4.clicked.connect(self.logout)
        self.main_window_admin_ui.show()

    def show_main_window_user(self):
        from window.MainWindowUI import MainWindowUI
        self.main_window_ui = MainWindowUI()
        self.main_window_ui.ui.pushButton_2.clicked.connect(self.show_profile_page)
        self.main_window_ui.ui.pushButton_3.clicked.connect(self.show_appointment_page)
        self.main_window_ui.ui.pushButton_4.clicked.connect(self.logout)
        self.main_window_ui.ui.pushButton.clicked.connect(self.show_history_page)
        self.main_window_ui.show()

    def show_add_user(self):
        from window.Add_UserUI import Add_UserUI
        self.add_user_ui = Add_UserUI()
        self.add_user_ui.ui.pushButton.clicked.connect(self.add_user)
        self.add_user_ui.ui.pushButton_2.clicked.connect(self.show_main_window_admin)
        self.add_user_ui.show()

    def add_user(self):
        # Implement logic to add a new user here
        # For simplicity, let's assume the user is added successfully
        # Replace this with your actual user addition logic
        self.show_main_window_admin()

    def show_profile_page(self):
        # Implement logic to show the profile page here
        pass

    def show_appointment_page(self):
        # Implement logic to show the appointment page here
        pass

    def show_log_page(self):
        # Implement logic to show the log page here
        pass

    def show_list_doctor_page(self):
        # Implement logic to show the list doctor page here
        pass

    def show_list_nurse_page(self):
        # Implement logic to show the list nurse page here
        pass

    def show_list_patient_page(self):
        # Implement logic to show the list patient page here
        pass

    def show_history_page(self):
        # Implement logic to show the history page here
        pass

    def logout(self):
        self.show_login()

