# CREATE A LIST OF CARS

cars = [
    'audi',
    'bmw',
    'subaru',
    'toyota']

# CREATE A FOR LOOP THAT PRINTS BMW ALL UPPER CASE AND THE REST JUST TITLE

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())