# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
magic = 'abracadabra'
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))
# Advanced Slicing:
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet.find("hij"))
print(alphabet[5:7])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:12:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
speech = "not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(speech.find("John F. Kennedy"))
print(speech[79:94])
# Manipulating Words:
words = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(words.find("subjective"))
print(words[36:46])
# b. Extract every third word.
print(words[::3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(words.replace('good', 'fun'))
# Problem Set 3: String Methods
# Upper & Lower:
phrase ="MAY THE FORCE BE WITH YOU."
result=phrase.lower()
print(result)
# String Joining and Splitting:
# motto = ["Make", "haste", "slowly."],
# # a. Convert the list into a single string.
# result = " ".join(motto)
# print(result)
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
sentence = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(sentence.replace('busy', 'distracted'))
# b. Replace "plans" with "mistakes".
print(sentence.replace('plans', 'mistakes'))
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
word = "Iteration"
concatenated = word * 7
print("Concatenated Word:", concatenated)
# Word Search:
text=  "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
search_word = "moonlight"
is_present = search_word in text
print("Does 'moonlight' appear in the quote?", is_present)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
phrase = "Supercalifragilisticexpialidocious"
length = len(phrase)
print("Number of characters:", length)
# b. Count the number of times the letter 'i' appears in the same word/phrase.
count_i = phrase.count('i')
print("Number of times 'i' appears:", count_i)
