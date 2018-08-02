# We won't be running this script. Instead we will import it into our python and run the functions ourself.

def break_words(stuff):
    """This function will break up words for us. """
    words = stuff.split(" ")
    return words
    
def sort_words(words):
    """Sort the words."""
    return sorted(words)
    
def print_first_word(words):
    """print the first word after poping it off."""
    word = words.pop(0)
    print word
        
def print_last_word(words):
    """print the last word after poping it off."""
    word = words.pop(-1)
    print word
        
def sort_sentence(sentence):
    """takes in a full sentence and return the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
"""
Import this filename on terminal. give a string value to sentence " ". give words = filename.functionname(parameter). This is the standard way of importing your py file as module and using its function.String-sorted based on ASCII translations like [4, 6, 3, 5, 1] will be sorted as [1, 3, 4, 5, 6]. you can also reverse sort.for printing first word pop(0) & pop(-1 ) for last word.

"""
