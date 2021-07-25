# WRITE A PROGRAM THAT DETERMINES WHETHER OR NOR A NUMBER IS A MULTIPLE OF TEN
number = input("Please enter a number and I'll tell you if it is a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of ten!")
else:
    print(f"The number {number} is not a multiple of ten!")