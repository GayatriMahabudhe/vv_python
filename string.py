#1) Count vowels, consonants, digits, and special characters

def count_categories(s):
    vowels = "aeiouAEIOU"
    vowel_count = consonant_count = digit_count = special_count = 0

    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif ch.isdigit():
            digit_count += 1
        elif not ch.isspace():  # spaces are ignored; count other special chars
            special_count += 1

    return vowel_count, consonant_count, digit_count, special_count

text = "Hello, Pune 411001! #Vodafone"
v, c, d, sc = count_categories(text)
print(f"Vowels: {v}, Consonants: {c}, Digits: {d}, Special: {sc}")

#2) Reverse each word individually (keep word order)
def reverse_each_word(s):
    words = s.split()                     # split by spaces
    reversed_words = [w[::-1] for w in words]  # reverse each word using slicing
    return " ".join(reversed_words)
text = "Python strings are fun"
print(reverse_each_word(text))

#3) Check palindrome using indexing/slicing
def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
print(is_palindrome("Level"))
print(is_palindrome("Never odd or even"))
print(is_palindrome("Vodafone"))

#4) Frequency of each character in a string
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
text = "hello world"
freq_map = char_frequency(text)
for ch, count in freq_map.items():
    print(f"'{ch}': {count}")

#5) Demonstrate string immutability and handle the error
def demonstrate_immutability():
    s = "Vodafone"
    try:
        # Strings are immutable: this will raise a TypeError
        s[0] = 'v'
    except TypeError as e:
        print("Caught error:", e)
        # Correct way: create a new string
        s = 'v' + s[1:]
        print("Modified by creating a new string:", s)
demonstrate_immutability()



