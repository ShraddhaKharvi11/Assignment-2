#Text Analysis Function

# Count words
def count_words(text):
    words=text.split()
    return len(words)

# Count vowels
def count_vowels(text):
    vowels='aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

# Count consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

def reverse_text(text):
    return text[::-1]

# Check palindrome (ignore case & spaces)
def is_palindrome(text):
    processed = text.replace(" ", "").lower()
    return processed == processed[::-1]

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

# Word frequency dictionary
def word_frequency(text):
    freq = {}
    words = text.lower().split()

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


# Find longest word
def longest_word(text):
    words = text.split()
    if not words:
        return "", 0

    longest = max(words, key=len)
    return longest, len(longest)

def analyze_text(text):

    print("\n=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    palindrome_result = "Yes" if is_palindrome(text) else "No"
    print("Palindrome:", palindrome_result)

    print("Without vowels:", remove_vowels(text))

    word, length = longest_word(text)
    print(f"Longest word: {word} ({length} letters)")

    freq = word_frequency(text)
    freq_output = ", ".join(f"{k}: {v}" for k, v in freq.items())
    print("Word Frequency:", freq_output)


# -------- Program Start --------
user_text = input("Enter text: ")
analyze_text(user_text)