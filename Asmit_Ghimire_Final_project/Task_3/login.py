import codecs

def login(username, password):
    with open("passwd.txt", "r") as file:
        for line in file:
            parts = line.strip().split(':')
            if parts[0] == username and parts[2] == codecs.encode(password, 'rot_13'):
                print("Access granted.")
                return

    print("Access denied.")

if __name__ == "__main__":
    username = input("User:     ")
    password = input("Password: ")
    login(username, password)
