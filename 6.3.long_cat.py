import string

text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

"""

:param param1: this is the text
:returns: a dictionary of all the words in the text as the keys and all their lenghts as values
"""
def count_words(text):
    only_letters=list(ch for ch in text if ch.isalpha() or ch==' ' or ch=='\n')
    only_letters = ''.join(only_letters).split()
    dic={word:len(word) for word in only_letters}
    return dic

print(count_words(text))

