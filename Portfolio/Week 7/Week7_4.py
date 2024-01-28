"""one approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is trick"""

def frequency_analysis(message):

    letter_counts = {}

    for char in message.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    top_six_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)[:6]

    result_dict = dict(top_six_letters)

    return result_dict

encrypted_message = "This is an example encrypted message. E is one of the most common letters."
result = frequency_analysis(encrypted_message)

print("Six most common letters and their counts:")
for letter, count in result.items():
    print(f"{letter}: {count}")