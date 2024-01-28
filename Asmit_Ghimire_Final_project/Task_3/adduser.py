import codecs

def add_user(username, real_name, password):
    with open("passwd.txt", "a") as file:
        # Encrypt the password using ROT-13
        encrypted_password = codecs.encode(password, 'rot_13')
        file.write(f"{username}:{real_name}:{encrypted_password}\n")
    print("User Created.")

if __name__ == "__main__":
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = input("Enter password: ")
    add_user(username, real_name, password)
