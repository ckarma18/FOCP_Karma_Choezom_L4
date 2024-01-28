import sys

PASSWORD_FILE = "passwd.txt" 

def read_users_data(): 
    with open(PASSWORD_FILE, "r") as file:
        lines = file.readlines()
    return [line.strip().split(":") for line in lines]

def write_users(users): 
    with open(PASSWORD_FILE, "w") as file:
        for user in users:
            file.write(":".join(user) + "\n")

def user_login():
    users = read_users_data()

    username = input("enter your username: ").strip().lower()
    password = input("enter your password: ").strip().lower()

    if any(user[0] == username and user[2] == password for user in users):
        print("access granted.\nWELCOME", username)
    else:
        print("access denied")

def add_user():
    users = read_users_data()

    username = input("enter your username: ").strip().lower()
    real_name = input("enter your real name: ").strip().lower()
    password = input("enter your password: ").strip().lower()

    if any(user[0] == username for user in users):
        print("user already exists")
    else:
        users.append([username, real_name, password])
        write_users(users)
        print("user created.")


def delete_user():
    users = read_users_data()

    username = input("enter your username: ").strip().lower()
    password = input("enter your password: ").strip().lower()

    if any(user[0] == username and user[2] == password for user in users):
        users = [user for user in users if user[0] != username]
        write_users(users)
        print("user deleted.")
    else:
        print("user not found")


def change_passwd():
    users = read_users_data()

    username = input("enter your username: ").strip().lower()
    user_index = next((i for i, user in enumerate(users) if user[0] == username), None)

    if user_index is not None:
        current_password = input("Current Password: ").strip()
        new_password = input("New Password: ").strip()
        confirm_password = input("Confirm: ").strip()

        if users[user_index][2] == current_password and new_password == confirm_password:
            users[user_index][2] = new_password
            write_users(users)
            print("Password changed.")
        else:
            print("password ont match please try again")
            change_passwd()
    else:
        print("user not found.")

if len(sys.argv) != 2:
    print("\n\n please enter the function you want to use:\n we have 4 of them \n login, adduser, deluser, passwd\n\n")
    sys.exit(1)

function = sys.argv[1]

if function == 'login':
    user_login()
elif function == 'adduser':
    add_user()
elif function == 'deluser':
    delete_user()
elif function == 'passwd':
    change_passwd()
else:
    print("\n\n please enter the function you want to use:\n we have 4 of them \n login, adduser, deluser, passwd\n\n")
    sys.exit(1)
