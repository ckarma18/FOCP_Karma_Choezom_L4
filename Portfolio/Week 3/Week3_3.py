""" Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long."""

passw1=input("enter new pass word: ")
passw2=input("enter password: ")
if passw1==passw2 and len(passw1)>=8 and len(passw2)>=12:
    print("password set")
else:
    print("error") 