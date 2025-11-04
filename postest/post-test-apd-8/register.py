from data import user

def register():
    username = input("Buat username: ")
    password = input("Buat password: ")

    if username in user:
        print("Username sudah dipakai!\n")
    else:
        user[username] = {"password": password}
        print(f"User '{username}' berhasil dibuat!\n")