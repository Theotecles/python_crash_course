# CREATE A LIST OF DIFFERENT KINDS OF BICYCLES

bicycles = ['trek',
			'cannondale',
			'redline',
			'specialized']

# PRINT THE WHOLE LIST

print(bicycles)

# PRINT THE FIRST ELEMENT OF THE LIST

print(bicycles[0])

# CAPITALIZE THE FIRST LETTER OF THE FIRST ELEMENT OF THE LIST

print(bicycles[0].title())

# PRINT THE SECOND AND FOURTH ELEMENT FROM THE LIST

print(bicycles[1])
print(bicycles[3])

# PRINT THE LAST ITEM FROM THE LIST

print(bicycles[-1])

# TAKE AN ELEMENT FROM THE LIST AND USE IT IN A MESSAGE

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)