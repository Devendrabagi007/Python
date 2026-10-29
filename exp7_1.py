#checking the valid and invalid phone numbers
#import re

#phone = input("Enter the valid phone number :-")

#if re.fullmatch(r"[0-9]{10}",phone):
#    print("valid phone number")
#else:
#    print("Invalid phone number")

#re search module eg
#import re

#sentence = input("Enter the sentence:")

#result = re.search(r"\bdevendra\b",sentence)

#if result:
#    print("Word found:",result.group())
#    print("starting position:",result.start())
#else:
#    print("word doesn't exsists")

#Text processing problem
#text = input("Enter a sentence: ")

#print("Original text:", text)

#print("Number of characters:", len(text))

#words = text.split()
#print("Number of words:", len(words))

#print("Uppercase:", text.upper())
#print("Lowercase:", text.lower())

#old_word = input("Enter the word to replace: ").strip()
#new_word = input("Enter the new word: ").strip()

#updated_text = text.replace(old_word,  new_word)
#print("Updated text:", updated_text)

#re match problem
import re

sentence = input("Enter a sentence: ")

result = re.match(r"\bPython\b", sentence)

if result:
    print("The sentence starts with Python.")
    print("Matched word:", result.group())
else:
    print("The sentence does not start with Python.")
