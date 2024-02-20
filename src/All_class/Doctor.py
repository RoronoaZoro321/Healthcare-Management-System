from .Staff import Staff

class Doctor(Staff):
    def __init__(self, fname: str, lname: str, address: str, phone_number: str, password: str ,employee_id: str, 
                 department: str, role: str, specialty: list[str], 
                 qualifications: str, salary: int):
        super().__init__(fname, lname,address, phone_number, password, employee_id, department, role)
        self.specialty = specialty
        self.qualifications = qualifications
        self.salary = salary
    
    def get_id(self):
        return self.employee_id
        
    def update_schedule(self):
        pass
    
    def select_nurse(self):
        pass
    
    def patient_report(self):
        pass

    def update_attributes(self, new_data):
        """
        Updates the Doctor object's attributes with the provided data.

        Args:
            new_data (list): A list of new values corresponding to the Doctor's attributes.
                The order and meaning of the values should match your specific data structure.

        Raises:
            ValueError: If the number of provided values doesn't match the expected number of attributes.
        """
        
        if len(new_data) != len(self.__dict__) - 2:  # Adjust for inherited attributes
            raise ValueError("Number of provided values doesn't match expected number of attributes.")

        # Update attributes based on their position in the list and your data structure
        for i, value in enumerate(new_data):
            attribute_name = list(self.__dict__.keys())[i + 2]  # Skip inherited attributes
            setattr(self, attribute_name, value)