# CREATE A LIST OF GUESTS

guests = ['Albert Camus',
		  'Plato',
		  'Julius Caesar',
		  'Tom Hanks']

# ADD NEW GUESTS TO THE LIST

guests.insert(0, 'Ronald Reagan')
guests.insert(2, 'Barack Obama')
guests.append('Jon Favreau')

# CREATE A MESSAGE STATING THE NUMBER OF PEOPLE ATTENDING THE DINNER

message = f"Just so you are all aware there will be {len(guests)} people attending the dinner this evening."
print(message)