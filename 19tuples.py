stuff = raw_input('>> Enter input:  ')
words = stuff.split()  # breaking sentence into words.

"""A tuple is nothing more than a list that you can’t modify. It’s created by putting data inside two () with a comma, like a list. """

first_word = ('direction', 'north')   # (TOKEN, WORD)
second_word = ('verb'. 'go')
sentence = [first_word, second_word]

# dealing with exception
def convert_number(words):
    try:
        return int(words)
    except ValueError:
        return None



