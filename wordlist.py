import random

words = [

]

def get_random_word():
    """
    Επιλέγει τυχαία μία λέξη από τη λίστα για χρήση ως λέξη-στόχος.
    Returns:
        str: Η επιλεγμένη λέξη.
    """
    word = random.choice(words)
    print(word)
    return word
