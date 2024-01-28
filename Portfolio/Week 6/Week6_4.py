"""4. Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way.
"""


def simple_encrypt(message):
    encrypted_message = ''.join(message.split())[::-1]
    return encrypted_message

original_message = input("Enter a message to encrypt: ")
encrypted_message = simple_encrypt(original_message)

print(f"Encrypted Message: {encrypted_message}")
