# DEFINE A TUPLE

dimensions = (200, 50)

# PRINT EACH ELEMENT OF THE TUPLE

print(dimensions[0])
print(dimensions[1])

# LOOP OVER VALUES IN A TUPLE USING A FOR LOOP

for dimension in dimensions:
	print(dimension)

# REDEFINE THE ENTIRE TUPLE

print("Original Dimensions")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 50)
print("Modified Dimensions")
for dimension in dimensions:
	print(dimension)