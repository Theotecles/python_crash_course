# CREATE A FUNCTION THAT ACCEPTS A LIST OF THINGS THAT SOMEONE WANTS ON A SANDWICH
def make_sandwich(*items):
    """ CREATES A FUNCTION THAT BUILDS SANDWICH ORDERS"""
    print("\nMaking your sandwich...")
    for item in items:
        print(f"\nAdding {item}...")
    print("\nYour sandwich is ready!")

make_sandwich('salami', 'lettuce', 'onion', 'mustard')
make_sandwich('turkey', 'lettuce', 'tomatoe')
make_sandwich('ham', 'cheese')