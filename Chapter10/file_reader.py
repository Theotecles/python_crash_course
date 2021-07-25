# OPEN AND PRINT THE CONTENTS OF A TEXT DOCUMENT
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())

# OPEN AND PRINT THE CONTENTS OF EACH LINE OF A TEXT DOCUMENT
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# OPEN AND STORE THE CONTENTS OF A TEXT DOCUMENT IN A LIST
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# WORK WITH THE CONTENTS IN A TEXT DOCUMENT
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# USE A BIGGER FILE
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# CHECK TO SEE IF MY BIRTHDAY IS IN PI
birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi")