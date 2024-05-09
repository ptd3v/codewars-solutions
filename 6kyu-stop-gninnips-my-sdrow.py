# Stop gninnipS My sdroW! (6th Kyu)
# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed

# Functions Required: split(),join(), len(), if/else, [::]

# My Solution:
def spin_words(sentence):
    spun = []
    for word in sentence.split():
        if len(word) >= 5:
            spun.append(word[::-1])
        else:
            spun.append(word)
    return " ".join(spun)

# List Comprehension:
def spin_words(sentence):
    def spun(word):
        return word if len(word) < 5 else word[::-1]

    return " ".join(spun(word) for word in sentence.split())

# Community Solution:
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])