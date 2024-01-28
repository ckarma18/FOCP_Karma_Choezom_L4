"""s e n d c h e e s e
sxyexynxydxy cxyhxyexyexysxye
6. Write a program that decrypts messages encoded as above."""

def decrypt_message(encrypted_message, interval_used):
    decrypted_message = ''
    j = 1 
    
    for i, char in enumerate(encrypted_message):
        if char.isalpha():
            decrypted_message += char
            j = (j + 1) % interval_used
        else:
            if j == 0:
                decrypted_message += char
            else:
                j = (j + 1) % interval_used

    return decrypted_message


encrypted_message = input("Enter the encrypted message: ")
interval_used = int(input("Enter the interval used: "))

decrypted_message = decrypt_message(encrypted_message, interval_used)
print(f"Decrypted Message: {decrypted_message}")