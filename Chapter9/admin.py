from users import User

# CREATE A CLASS CALLED PRIVILEGES
class Privileges:
    """ATTEMPT TO MODEL PRIVILEGES"""
    def __init__(self, privileges=[
                           'can add post',
                           'can delete post',
                           'can ban user'
                           ]):
        """INITIALIZE DIFFERENT ATTRIBUTES FOR PRIVILEGES"""
        self.privileges = privileges
    def show_privileges(self):
        print("The user has the following privileges:")
        for privilege in self.privileges:
            print(privilege)

# CREATE A CLASS CALLED ADMIN THAT INHERITS FROM THE USER CLASS
class Admin(User):
    def __init__(self, first_name, last_name, city, country, age):
        """
        INITIALIZE ATTRIBUTES OF THE PARENT CLASS.
        THEN INITIALIZE ATTRIBUTES SPECIFIC TO ADMIN
        """
        super().__init__(first_name, last_name, city, country, age)
        self.privileges = Privileges()