def print_contents(filename):
    """THIS WILL PRINT THE CONTENTS OF A FILE"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print_contents(filename)