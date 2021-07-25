# PRINT NUMBERS 1 THROUGH 20

for value in range(1, 21):
	print(value)

# PRINT NUMBERS 1 THROUGH 1 MILLION

for value in range (1, 1_000_001):
	print(value)

# MAKE A LIST OF NUMBERS 1 THROUGH 1 MILLION

numbers = []

for value in range(1, 1_000_001):
	numbers.append(value)

# PERFORM SIMPLE STATISTICS ON THIS LIST

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# MAKE A LIST OF ODD NUMBERS FROM 1 THROUGH 20

odd_numbers = [value for value in range(1, 20, 2)]

for number in odd_numbers:
	print(number)

# MAKE A LIST OF MULTIPLES OF 3 FROM 3 TO 30

by_threes = [value for value in range(3, 31, 3)]
for number in by_threes:
	print(number)

# MAKE A LIST OF NUMBERS 1 THROUGH 10 CUBED

cubed = []

for value in range(1, 11):
	cubed.append(value ** 3)

for number in cubed:
	print(number)

# USE LIST COMPREHENSION TO REMAKE CUBED

cubed =[value ** 3 for value in range(1, 11)]

for number in cubed:
	print(number)