    def test_doctor(self):
        d = Doctor("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role", 
                   ["specialty1", "specialty2"], "qualification", 100000)
        assert d.employee_id == 1234
        assert d.salary == 100000

    def test_nurse(self):
        n = Nurse("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role", 
                   ["specialty1", "specialty2"], "qualification", 100000)
        assert n.employee_id == 1234
        assert n.salary == 100000

    def test_admin(self):
        a = Admin("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role", 
                   ["specialty1", "specialty2"], "qualification", 100000)
        assert a.employee_id == 1234
        assert a.salary == 100000
    
    def test_appointment(self):
        p = Patient("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1)
        d = Doctor("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role", 
           ["specialty1", "specialty2"], "qualification", 100000)
        n = Nurse("John", "Doe", "1234 Main St.", "123-456-7890", "password", 1234, ["dept1", "dept2"], "role", 
           ["specialty1", "specialty2"], "qualification", 100000)
        a = Appointment(1,p,d,False,)