import re

text = input()

# Match words starting with a capital letter (A–Z), followed by 0 or more lowercase/uppercase letters
capital_words = re.findall(r'\b[A-Z][a-zA-Z]*\b', text)

for word in capital_words:
    print(word)
