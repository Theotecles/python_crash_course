# CREATE A DICTIONARY THAT DEFINES ALIEN 0
alien_0 = {'color': 'green', 'points': 5}

# PRINT WHAT EACH VALUE THE ALIEN HAS
print(alien_0['color'])
print(alien_0['points'])

# PRINT THE VALUE OF POINTS IN A STATEMENT
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# ADD NEW VALUES TO THE DICTIONARY
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# START WITH AN EMPTY DICTIONARY
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# MODIFY VALUES IN A DICTIONARY
print(f"The alien is the color {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# A MORE INTERESTING EXAMPLE THAT MOVES THE ALIEN'S POSITION
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# MOVE THE ALIEN TO THE RIGHT
# DETERMINE HOW FAR TO MOVE IT BASED OFF ITS CURRENT SPEED
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # THIS ALIEN MUST BE FAST
    x_increment = 3

# THE NEW POSITION IS THE OLD POSITION PLUS THE INCREMENET
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# REMOVE KEY VALUE PAIRS
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)