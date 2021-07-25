# WRITE A PROGRAM THAT POLLS PEOPLE ON WHY THEY LIKE PROGRAMMING
filename = 'programming_poll.txt'

polling = True

while polling == True:
    answer = input("Why do you like programming? (Enter 'q' to quit) ")
    if answer == 'q':
        polling = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{answer}\n")