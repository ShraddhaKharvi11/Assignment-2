# String Manipulator

# Taking sentence input from user
sentence=input("Enter a sentence: ")

# Printing Original sentence
print("\nOriginal:",sentence)

# Printing total words including spaces
print("Characters (with spaces):",len(sentence))

# Printing total words excluding spaces
print("Characters (without spaces):",len(sentence.replace(" ","")))

# Splitting sentence into words taking space as separator
words=sentence.split()

# Number of words in sentence
print("Words:",len(words))

# String case conversions
print("UPPERCASE:",sentence.upper())
print("lowercase:",sentence.lower())
print("Title Case:",sentence.title())

print("First word:",words[0])
print("Last word:",words[-1])

# Reversing sentence using slicing
print("Reversed:",sentence[::-1])
