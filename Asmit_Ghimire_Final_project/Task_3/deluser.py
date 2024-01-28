import codecs

def delete_user(username):
    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    found = False
    with open("passwd.txt", "w") as file:
        for line in lines:
            if not line.startswith(f"{username}:"):
                file.write(line)
            else:
                found = True

    if found:
        print("User Deleted.")
    else:
        print("Cannot delete. Most likely username not found.")

if __name__ == "__main__":
    username = input("Enter username: ")
    delete_user(username)

