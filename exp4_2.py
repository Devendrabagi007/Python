#String-Problem-statement-list
#1.Write a program to input a string and display its length without using the len() function.
 
#text = input("Enter the Sting:-")

#count = 0
#for char in text:
	#count = count + 1
#print("The length of string is:",count)

#2.Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 

#text = input("Enter the string:-")

#vowels = 0
#consonants = 0
#digits = 0
#spaces = 0
#special = 0

#for char in string:
   # if char.lower() in "aeiou":
        #vowels += 1
   # elif char.isalpha():
       # consonants += 1
    #elif char.isdigit():
       # digits += 1
   # elif char.isspace():
      #  spaces += 1
   # else:
       # special += 1

#print("Vowels:", vowels)
#print("Consonants:", consonants)
#print("Digits:", digits)
#print("Spaces:", spaces)
#print("Special characters:", special)


#3.Reverse the given string without using built-in reverse functions. 
# s = input("Enter a string: ")

# reversed_string = ""

# for i in range(len(s) - 1, -1, -1):
#     reversed_string += s[i]

# print("Reversed string:", reversed_string)


# # 4. Palindrome Check
# s = input("Enter a string: ")
# if s == s[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


# # 5. Uppercase and Lowercase Count
# s = input("Enter a string: ")
# upper_count = 0
# lower_count = 0
# for char in s:
#     if char.isupper():
#         upper_count += 1
#     elif char.islower():
#         lower_count += 1
# print("Uppercase count:", upper_count)
# print("Lowercase count:", lower_count)


# # 6. Replace Characters
# s = input("Enter a string: ")
# old_char = input("Enter character to replace: ")
# new_char = input("Enter new character: ")
# print("Replaced string:", s.replace(old_char, new_char))


# # 7. Remove Spaces
# s = input("Enter a string: ")
# print("String without spaces:", s.replace(" ", ""))


# # 8. Frequency of a Character
# s = input("Enter a string: ")
# char = input("Enter character to find frequency: ")
# print(f"Frequency of '{char}':", s.count(char))


# # 9. First and Last Character
# s = input("Enter a string: ")
# if len(s) > 0:
#     print("First character:", s[0])
#     print("Last character:", s[-1])
# else:
#     print("String is empty.")


# # 10. ASCII Values
# s = input("Enter a string: ")
# print("ASCII values:")
# for char in s:
#     print(f"'{char}': {ord(char)}")


# # 11. Word Count
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print("Total number of words:", len(words))


# # 12. Longest Word
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# if words:
#     longest = max(words, key=len)
#     print("Longest word:", longest)
# else:
#     print("No words entered.")


# # 13. Shortest Word
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# if words:
#     shortest = min(words, key=len)
#     print("Shortest word:", shortest)
# else:
#     print("No words entered.")


# # 14. Title Case
# sentence = input("Enter a sentence: ")
# print("Title case:", sentence.title())


# # 15. Duplicate Characters
# s = input("Enter a string: ")
# seen = set()
# duplicates = set()
# for char in s:
#     if char in seen:
#         duplicates.add(char)
#     else:
#         seen.add(char)
# print("Duplicate characters:", list(duplicates))


# # 16. Character Frequency
# s = input("Enter a string: ")
# freq = {}
# for char in s:
#     freq[char] = freq.get(char, 0) + 1
# print("Character frequency:")
# for char, count in freq.items():
#     print(f"'{char}': {count}")


# # 17. Anagram Check
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# if sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", "")):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")


# # 18. Remove Duplicate Characters
# s = input("Enter a string: ")
# result = ""
# for char in s:
#     if char not in result:
#         result += char
# print("String after removing duplicates:", result)


# # 19. Substring Search
# main_str = input("Enter main string: ")
# sub_str = input("Enter substring: ")
# if sub_str in main_str:
#     print(f"'{sub_str}' exists in the main string.")
# else:
#     print(f"'{sub_str}' does not exist in the main string.")


# # 20. Count Occurrences of a Word
# sentence = input("Enter a sentence: ")
# word = input("Enter word to count: ")
# words = sentence.split()
# print(f"The word '{word}' appears {words.count(word)} times.")


# # 21. Password Validator
# password = input("Enter password: ")
# has_upper = any(c.isupper() for c in password)
# has_lower = any(c.islower() for c in password)
# has_digit = any(c.isdigit() for c in password)
# has_special = any(not c.isalnum() for c in password)

# if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
#     print("Valid password")
# else:
#     print("Invalid password")


# # 22. Run-Length Encoding
# s = input("Enter a string (e.g. aaabbccccd): ")
# encoded = ""
# if s:
#     count = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             encoded += s[i - 1] + str(count)
#             count = 1
#     encoded += s[-1] + str(count)
# print("Run-Length Encoded string:", encoded)


# # 23. String Compression
# s = input("Enter a string: ")
# compressed = ""
# if s:
#     count = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             compressed += s[i - 1] + str(count)
#             count = 1
#     compressed += s[-1] + str(count)

# if len(compressed) < len(s):
#     print("Compressed string:", compressed)
# else:
#     print("Original string:", s)


# # 24. Most Frequent Character
# s = input("Enter a string: ")
# if s:
#     freq = {}
#     for char in s:
#         freq[char] = freq.get(char, 0) + 1
#     most_freq = max(freq, key=freq.get)
#     print(f"Most frequent character: '{most_freq}' with frequency {freq[most_freq]}")
# else:
#     print("Empty string.")


# # 25. Second Most Frequent Character
# s = input("Enter a string: ")
# if s:
#     freq = {}
#     for char in s:
#         freq[char] = freq.get(char, 0) + 1
#     sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
#     if len(sorted_freq) >= 2:
#         print(f"Second most frequent character: '{sorted_freq[1][0]}' with frequency {sorted_freq[1][1]}")
#     else:
#         print("Not enough unique characters.")
# else:
#     print("Empty string.")


# # 26. Caesar Cipher
# text = input("Enter text to encrypt: ")
# shift = int(input("Enter shift value: "))

# def caesar_encrypt(text, shift):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             base = ord('A') if char.isupper() else ord('a')
#             result += chr((ord(char) - base + shift) % 26 + base)
#         else:
#             result += char
#     return result

# encrypted = caesar_encrypt(text, shift)
# decrypted = caesar_encrypt(encrypted, -shift)

# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)


# # 27. Email Validator
# import re
# email = input("Enter email address: ")
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# if re.match(pattern, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")


# # 28. Word Frequency Dictionary
# paragraph = input("Enter a paragraph: ")
# words = paragraph.lower().split()
# word_freq = {}
# for word in words:
#     cleaned = word.strip(".,!?;:\"'")
#     if cleaned:
#         word_freq[cleaned] = word_freq.get(cleaned, 0) + 1
# print("Word Frequency Dictionary:", word_freq)


# # 29. Sentence Reversal
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print("Reversed sentence:", " ".join(words[::-1]))


# # 30. String Rotation
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# if len(str1) == len(str2) and len(str1) > 0 and str2 in (str1 + str1):
#     print("Output: Yes")
# else:
#     print("Output: No")



