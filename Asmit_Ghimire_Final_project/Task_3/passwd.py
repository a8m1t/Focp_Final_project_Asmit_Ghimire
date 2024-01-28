import codecs

def change_password(username, current_password, new_password):
    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    encrypted_current_password = codecs.encode(current_password, 'rot_13')
    encrypted_new_password = codecs.encode(new_password, 'rot_13')

    found = False
    with open("passwd.txt", "w") as file:
        for line in lines:
            if line.startswith(f"{username}:") and line.endswith(f"{encrypted_current_password}\n"):
                file.write(f"{username}:{line.split(':')[1]}:{encrypted_new_password}\n")
                found = True
            else:
                file.write(line)

    if found:
        print("Password changed.")
    else:
        print("Cannot change password. Most likely username or current password is incorrect.")

if __name__ == "__main__":
    username = input("User:             ")
    current_password = input("Current Password: ")
    new_password = input("New Password:     ")
    confirm_password = input("Confirm:          ")

    if new_password == confirm_password:
        change_password(username, current_password, new_password)
    else:
        print("Passwords do not match.")
