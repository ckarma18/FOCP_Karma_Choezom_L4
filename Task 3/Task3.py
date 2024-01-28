def create_user(username, real_name, password):
    with open('passwd.txt', 'a') as file:
        file.write(f'{username}:{real_name}:{password}\n')
    print("User Created.")

if __name__ == "__main__":
    new_username = input("Enter new username: ")
    new_real_name = input("Enter real name: ")
    new_password = input("Enter password: ")

    with open('passwd.txt', 'r') as file:
        existing_users = [line.split(':')[0] for line in file.readlines()]

    if new_username in existing_users:
        print("Cannot add. Most likely username already exists.")
    else:
        create_user(new_username, new_real_name, new_password)

def change_password(username, current_password, new_password):
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()

    with open('passwd.txt', 'w') as file:
        for line in lines:
            fields = line.split(':')
            if fields[0] == username and fields[2].strip() == current_password:
                file.write(f'{fields[0]}:{fields[1]}:{new_password}\n')
                print("Password changed.")
            else:
                file.write(line)

if __name__ == "__main__":
    user_to_change = input("User:             ")
    current_password = input("Current Password: ")
    new_password = input("New Password:     ")
    confirm_password = input("Confirm:          ")

    if new_password == confirm_password:
        modify_password(user_to_change, current_password, new_password)
    else:
        print("Passwords do not match. No change made.")

def perform_login(username, password):
    with open('passwd.txt', 'r') as file:
        for line in file:
            fields = line.split(':')
            if fields[0] == username and fields[2].strip() == password:
                return True
    return False

if __name__ == "__main__":
    login_username = input("User:     ")
    login_password = input("Password: ")

    if perform_login(login_username, login_password):
        print("Access granted.")
    else:
        print("Access denied.")
        
def delete_username(username):
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()

    with open('passwd.txt', 'w') as file:
        for line in lines:
            if not line.startswith(username + ":"):
                file.write(line)

    print("User Removed.")

if __name__ == "__main__":
    delete_username = input("Enter username: ")
    delete_username(delete_username)
