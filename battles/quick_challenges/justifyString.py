# Forgot to save code

idea = """

length = l

add words to "curline" with at least one space to the right (width = length + 1) while they do not exceed width

count available number of spaces (length minus words.replace(" ", ""))

add words from wordlist[:-1] and "spaces to use".

for i, word in enumerate(wordlist, 1):
    spaces_to_use = math.ceil(spaces_left / (num_words - i))
    justified += word + " " * spaces_to_use
    spaces_left -= spaces_to_use

then add the final word and ljust the whole thing
add it to the output
"""
