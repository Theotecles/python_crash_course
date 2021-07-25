# CREATE A LIST OF MAGICIAN NAMES

magicians = ['alice',
			 'david',
			 'carolina']

# CREATE A SIMPLE FOR LOOP THAT WILL ITERATE AND PRING EVERY NAME IN THE LIST
 
for magician in magicians:
	print(magician)

# CREATE A FOR LOOP THAT PRINTS A MESSAGE ALONG WITH THE NAME

for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")

# CREATE THE SAME FOR LOOP BUT ADD A SECOND MESSAGE TO IT

for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

# ADD A MESSAGE THAT ISNT INDENTED AND WILL ONLY EXECUT ONCE

for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")