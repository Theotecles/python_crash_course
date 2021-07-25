# CREATE A LIST OF GUESTS

guests = ['Albert Camus',
		  'Plato',
		  'Julius Caesar',
		  'Tom Hanks']

# ADD NEW GUESTS TO THE LIST

guests.insert(0, 'Ronald Reagan')
guests.insert(2, 'Barack Obama')
guests.append('Jon Favreau')

# REMOVE ALL GUESTS EXCEPT TWO LETTING THEM KNOW THEY ARE NO LONGER INVITED

popped_guest0 = guests.pop(0)
print(f"Dear {popped_guest0}\n\nI regret to inform you that you are no longer invited to dinner. Sorry, sucks to suck.")

popped_guest1 = guests.pop(1)
print(f"Dear {popped_guest1}\n\nI regret to inform you that you are no longer invited to dinner. Sorry, sucks to suck.")

popped_guest2 = guests.pop(1)
print(f"Dear {popped_guest2}\n\nI regret to inform you that you are no longer invited to dinner. Sorry, sucks to suck.")

popped_guest3 = guests.pop(1)
print(f"Dear {popped_guest3}\n\nI regret to inform you that you are no longer invited to dinner. Sorry, sucks to suck.")

popped_guest4 = guests.pop(1)
print(f"Dear {popped_guest4}\n\nI regret to inform you that you are no longer invited to dinner. Sorry, sucks to suck.")

# LET THE REMAINING PEOPLE KNOW THEY CAN STILL GO TO DINNER

print(f"Dear {guests[0]},\n\nUnfortunately, I had to tell a lot of people they couldnt come to dinner anymore, but you made the cut.")

print(f"Dear {guests[1]},\n\nUnfortunately, I had to tell a lot of people they couldnt come to dinner anymore, but you made the cut.")

# DELETE THE LAST TWO FROM THE LIST AND PRINT THE EMPTY LIST

del guests[0]
del guests[0]

print(guests)