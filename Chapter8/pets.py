# CREATE A FUNCTION CALLED DESCRIBE_PET
def describe_pet(animal_type, pet_name):
    """DISPLAY INFORMATION ABOUT PET"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'reggie')

describe_pet(animal_type='dog', pet_name='reggie')

def describe_pet(pet_name, animal_type='dog'):
    """DISPLAY INFORMATION ABOUT PET"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('reggie')

# A DOG NAMED REGGIE
describe_pet('reggie')
describe_pet(pet_name='reggie')

# A HAMSTER NAMED HARRY
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')