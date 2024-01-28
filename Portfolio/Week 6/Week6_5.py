"""5. Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fifth character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s e n d c h e e s e
sxyexynxydxy cxyhxyexyexysxye """

import random
import string

def random_interval_encryption(message):
    interval = random.randint(2, 20)
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=interval - len(message)))

    encrypted_message = ''
    j = 0
    for i, char in enumerate(message):
        if char.isalpha():
            encrypted_message += char + random_letters[j]
            j = (j + 1) % len(random_letters)
        else:
            encrypted_message += char

    return encrypted_message, interval

original_message = input("Enter a message to encrypt: ")
encrypted_message, interval_used = random_interval_encryption(original_message)

print(f"Encrypted Message: {encrypted_message}")
print(f"Interval Used: {interval_used}")
