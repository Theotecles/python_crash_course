# WRITE A PROGRAM THAT ASKS A USER FOR THEIR NAME AND PUTS IT IN A FILE
filename = 'guest_book.txt'

guest_book = True

while guest_book == True:
    name = input("What is your name? (Enter 'q' to quit) ")
    if name == 'q':
        guest_book = False
    else:
        guest_book = True

        with open(filename, 'a') as file_object:
            file_object.write(f"{name.title()}\n")