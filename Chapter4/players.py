# CREATE A LIST OF PLAYERS
players = ['charles',
		   'martina',
		   'michael',
		   'florence',
		   'eli']

# SLICE THE FIRST THREE PLAYERS FROM THE LIST

print(players[0:3])

# SLICE THE SECOND THIRD AND FOURTH ITEMS FROM THE LIST

print(players[1:4])

# SLICE THE FIRST THROUGH FOURTH ITEMS FROM THE LIST

print(players[:4])

# SLICE THE LAST THREE ITEMS FROM THE LIST

print(players[2:])

# SLICE THE LAST THREE ITEMS FROM THE LIST AGAIN

print(players[-3:])

# LOOP OVER THE FIRST THREE ELEMENTS OF THE LIST

print("Here are the players on my team:")

for player in players[:3]:
	print(player.title())