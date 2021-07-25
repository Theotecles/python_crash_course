# CREATE A LIST OF NUMBERS 1 THROUGH 9
numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
]

# CREATE A LOOP THAT PRINTS OUT THE NUMBER WITH ITS PROPER ORDINAL END
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")