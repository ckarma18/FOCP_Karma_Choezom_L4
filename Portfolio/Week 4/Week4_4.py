"""When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged."""

def remove_last_char(input_string):
    if len(input_string) > 1:
        return input_string[:-1]
    else:
        return input_string

user_input = input("Enter a string: ")
modified_string = remove_last_char(user_input)

print(f"Modified string: {modified_string}")