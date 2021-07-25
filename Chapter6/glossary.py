# CREATE A DICTIONARY OF PROGRAMMING WORDS AND THEIR DEFINITION
terms = {
    'dictionary': 'a set of values indicated with a key',
    'list': 'a set of values',
    'for loop': 'a method to iterate over something',
    'if-elif-else': 'conditions that can be set to perform certain actions or sequences',
    'sort': 'changes the order of a list',
    'method': 'a function which is defined inside a class body',
    'slice': 'an object usually containing a portion of a sequence',
    'statement': 'a statement is part of a suite',
    'type': 'the type of a python object determines what kind of object it is',
    'zen of python': 'listing of python design principles and philosopies'
}

# CREATE A LOOP THAT PRINTS EACH PIECE OF INFORMATION FROM THE DICTIONARY
for i, y in terms.items():
    print(f"{i.title()}: {y.title()}.\n")