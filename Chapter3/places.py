# CREATE A LIST OF PLACES I WOULD LIKE TO VISIT AND PRINT IT

places = ['niece',
		  'tokyo',
		  'marseilles',
		  'seoul',
		  'rome']

print(places)

# PRINT THE LIST IN ALPHABETICAL ORDER AND IN THE ORIGINAL ORDER

print(sorted(places))
print(places)

# PRINT THE LIST IN REVERSE ALPHABETICAL ORDER AND IN THE ORIGINAL ORDER

print(sorted(places, reverse=True))
print(places)

# REVERSE THE ORDER OF THE LIST

places.reverse()
print(places)

# CHANGE THE ORDER OF THE LIST BACK TO THE ORIGINAL ORDER

places.reverse()
print(places)

# CHANGE THE ORDER OF THE LIST TO ALPHABETICAL ORDER

places.sort()
print(places)

# CHANGE THE ORDER OF THE LIST TO REVERSE ALPHABETICAL ORDER

places.sort(reverse=True)
print(places)