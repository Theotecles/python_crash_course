dog = 'aussiedoodle'

print("Is the dog an aussiedoodle?")
print(dog == 'aussiedoodle')

print("\nIs the dog a german shepherd?")
print(dog == 'german shepherd')

print("\nIs the dog not an aussiedoodle?")
print(dog != 'aussiedoodle')

dog = 'german shepherd'

print("\nIs the dog not an aussiedoodle?")
print(dog != 'aussiedoodle')

name = 'JOHN'

print("\nIs this person's name John?")
print(name.lower() == 'john')

number = 13

print(number > 15)
print(number < 15)

number = 15

print(number >= 15)
print(number <= 14)

number_1 = 16
number_2 = 20

print("\nIs this person old enough to drive and also purchase alcohol?")
print(number_1 >= 16 and number_2 >= 21)

print("\nIs this person old enough to drive?")
print(number_1 >= 16 or number_2 >= 21)

dogs = [
    'aussiedoodle',
    'chocolate lab',
    'golden retriever',
    'french bulldog',
    'corgi'
]

print("\nAre Labrador Retrievers on my list of favorite dogs?")
print('labrador retriver' in dogs)

print("\nAre Pit Bulls not on my list of favorite dogs?")
print('pit bull' not in dogs)