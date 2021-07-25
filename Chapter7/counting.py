# CREATE WHILE LOOP TO COUNT FROM 1 TO 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# CREATE A WHILE LOOP THAT COUNTS FROM 1 TO 10 WITH ODD NUMBERS
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# AVOID INFINITE LOOPS
x = 1
while x <= 5:
    print(x)
    x += 1

# THIS LOOP RUNS FOREVER
x = 1
while x <= 5:
    print(x)