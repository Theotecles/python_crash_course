# SET A VALUE FOR AGE
age = 26

# WRITE AN IF-ELIF STATEMENT TO DETERMINE PERSONS STAGE OF LIFE
if age < 2:
    stage = 'baby'
if age < 4:
    stage = 'toddler'
if age < 13:
    stage = 'kid'
if age < 20:
    stage = 'teenager'
if age < 65:
    stage = 'adult'
if age >= 65:
    stage = 'elder'

print(stage.title())