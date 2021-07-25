# STORE THE FILE PATH AS FILENAME
filename = 'learning_python.txt'

# READ IN AND PRINT THE ENTIRE FILE
with open(filename) as file_object:
    contents = file_object.read()

print(contents.strip())

# PRINT EACH LINE OF THE DOCUMEENT
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# STORE THE FILE AS A LIST AND PRINT EACH LINE
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# REPLACE 'PYTHON' WITH 'C' IN EVERY LINE
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line.strip()
    print(line.replace('Python', 'C'))