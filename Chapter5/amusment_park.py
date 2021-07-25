# DEFINE AGE
age = 12

# CREATE AN IF STATEMENT FOR DIFFERENT PRICES BASED OFF AGE
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# MAKE THIS IF STATEMENT MORE CONCISE
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

# USE MULTIPLE ELIFS

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}")

# OMIT THE ELSE BLOCK

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}")