import sys
from PySide6.QtWidgets import QApplication
from database.db import initialize_database, addAdminAndDoctor, printInfo
from window.LoginUI import LoginUI


if __name__ == "__main__":
    initialize_database()
    addAdminAndDoctor()
    printInfo()

    app = QApplication(sys.argv)
    window = LoginUI()
    window.show()

    sys.exit(app.exec())

