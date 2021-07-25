# WRITE A PROGRAM THAT WILL ASK THEM HOW MANY PEOPLE THEY HAVE AND
# TELLS THEM WHETHER OR NOT A TABLE IS AVAILABLE
people = input("How many people will be dining with us today? ")
people = int(people)

if people > 8:
    print("Sorry, you are going to have to wait for a table.")
else:
    print("We have a table available!")