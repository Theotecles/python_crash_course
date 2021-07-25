# REPLACE THE FIRST ELEMENT OF THE LIST

motorcycles = ['honda',
			   'yamaha',
			   'suzuki']

print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# ADD ANOTHER ELEMENT TO THE LIST

motorcycles = ['honda',
			   'yamaha',
			   'suzuki']

print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# START WITH AN EMPTY LIST AND ADD ELEMENTS TO IT

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# ADD AN ELEMENT TO A CERTAIN PART OF THE LIST

motorcycles = ['honda',
			   'yamaha',
			   'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# REMOVE AN ELEMENT FROM A LIST

motorcycles = ['honda',
			   'yamaha',
			   'suzuki']

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda',
			   'yamaha',
			   'suzuki']

del motorcycles[1]
print(motorcycles)

# USING THE POP METHOD TO INTERACT WITH LISTS
# POP TAKES THE LAST ELEMENT OF THE LIST BUT ALLOWS YOU TO WORK WITH IT AFTER IT'S REMOVED

motorcycles = ['honda',
			   'yamaha',
			   'suzuki']

print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# USING THE POP METHOD
motorcycles = ['honda',
			   'yamaha',
			   'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

# THE POP METHOD CAN ALSO BE USED ON ANY ELEMENT OF THE LIST
motorcycles = ['honda',
			   'yamaha',
			   'suzuki']

first_owned = motorcycles.pop(0)
print(f"The motorcycle I owned was a {first_owned.title()}")

# REMOVE AN ITEM FROM THE LIST BY VALUE INSTEAD OF POSITION
motorcycles = ['honda',
			   'yamaha',
			   'suzuki',
			   'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# THE REMOVED VALUE CAN ALSO BE USED AFTER REMOVAL LIKE THE POP METHOD
motorcycles = ['honda',
			   'yamaha',
			   'suzuki',
			   'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

print(f"\nA {too_expensive.title()} is too expensive for me.")

# INTENTIONALLY GET AN INDEX ERROR BY REFERENCING AN ELEMENT OF THE LIST THAT DOESNT EXIST

motorcycles = ['honda',
			   'yamaha',
			   'suzuki']

print(motorcycles[3])