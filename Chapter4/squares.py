# CREATE A LIST OF NUMBERS 1 THROUGH 10 SQUARED

squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print(squares)

# WRITE THE SAME CODE MORE CONCISELY

squares = []
for value in range(1, 11):
	squares.append(value ** 2)

print(squares)

# DO SIMPLE STATISTICS ON THE CREATED LIST

print(min(squares))
print(max(squares))
print(sum(squares))

# USE A LIST COMPREHENSION TO CREATE THE SQUARES LIST

squares = [value ** 2 for value in range(1, 11)]
print(squares)