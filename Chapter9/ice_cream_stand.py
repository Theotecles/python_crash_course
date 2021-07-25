# CREATE A CLASS FOR A RESTAURANT
class Restaurant:
    """ATTEMPT TO DEFINE A SIMPLE RESTAURANT"""

    def __init__(self, name, cuisine_type):
        """INITIALIZE NAME AND CUISINE TYPE ATTRIBUTES"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ TELL THE NAME OF THE RESTAURANT AND THE TYPE OF FOOD IT SERVES"""
        print(f"The name of the restaurant is {self.name} and it serves {self.cuisine_type} food.")

    def open_or_close(self, operating=True):
        """ TELLS WHETHER OR NOT THE RESTAURANT IS OPEN OR CLOSED"""
        if operating==True:
            print(f"{self.name} is open for business!")
        else:
            print(f"{self.name} is currently closed. Please come back later")

    def set_number_served(self, served):
        """SETS THE VALUE FOR THE ATTRIBUTE NUMBER SERVED"""
        self.number_served = served

    def increment_number_served(self, served):
        """ADDS AMOUNT OF PEOPLE THAT WERE SERVED TO CURRENT TOTAL"""
        self.number_served += served

# CREATE A CLASS CALLED ICE CREAM STAND THAT INHERITS FROM RESTAURANT
class IceCreamStand(Restaurant):
    """REPRESENT ASPECTS OF RESTAURANT SPECIDIC TO ICECREAMSTAND"""
    def __init__(self, name, cuisine_type):
        """
        INITIALIZE ATTRIBUTES OF THE PARENT CLASS.
        THEN INITIALIZE ATTRIBUTES SPECIFIC TO AN ICECREAMSTAND
        """
        super().__init__(name, cuisine_type)
        self.flavors = ['vanilla',
                        'chocolate',
                        'strawberry'
                        ]
    def get_flavors(self):
        print(f"{self.name.title()} serves the following flavors of ice cream:")
        for flavor in self.flavors:
            print(flavor)

my_ice_cream_stand = IceCreamStand('graeters', 'ice cream')
my_ice_cream_stand.get_flavors()