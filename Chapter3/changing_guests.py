# CREATE A LIST OF GUESTS

guests = ['Albert Camus',
		  'Plato',
		  'Julius Caesar',
		  'Tom Hanks']

# INVITE EACH GUEST TO DINNER

print(f"Dear {guests[0]},\n\nYou are cordially invited to dinner at my house for a lovely meal.")
print(f"Dear {guests[1]},\n\nYou are cordially invited to dinner at my house for a lovely meal.")
print(f"Dear {guests[2]},\n\nYou are cordially invited to dinner at my house for a lovely meal.")
print(f"Dear {guests[3]},\n\nYou are cordially invited to dinner at my house for a lovely meal.")

# CHANGE THE LIST OF GUESTS AFTER HEARING PLATO CANT MAKE IT
# I'LL INVITE ARISTOTLE INSTEAD

guests[1] = 'Aristotle'

print(f"Dear {guests[0]},\n\nYou are cordially invited to dinner at my house for a lovely meal.")
print(f"Dear {guests[1]},\n\nYou are cordially invited to dinner at my house for a lovely meal.")
print(f"Dear {guests[2]},\n\nYou are cordially invited to dinner at my house for a lovely meal.")
print(f"Dear {guests[3]},\n\nYou are cordially invited to dinner at my house for a lovely meal.")
