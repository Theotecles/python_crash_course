def count_word(filename, word):
    """WILL COUNT HOW MANY TIMES A WORD APPEARS IN A CERTAIN TEXT"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry the file {filename} can't be found.")
    else:
        total_count = contents.lower().count(word)
        print(f"The word, {word}, appears in {filename} {total_count} times.")

filenames = [
    'great_gatsby.txt',
    'lord_of_rings.txt',
    'dracula.txt',
    'sherlock_holmes.txt'
]

for filename in filenames:
    count_word(filename, ' the ')