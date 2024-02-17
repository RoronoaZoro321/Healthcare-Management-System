# run this file to convert the .ui file to .py file
# Enter the UI file name here
file_name = "Add_User.ui"

# pyside6-uic ./src/gui/ui/Login.ui -o "src\gui\python\Login.py"
import subprocess
subprocess.run(["pyside6-uic", f"./src/gui/ui/{file_name}", "-o", f"src/gui/python/{file_name.split('.')[0]}.py"])

# for resource file
# pyside6-rcc resource.qrc -o resource_rc.py
# from . import resource_rc