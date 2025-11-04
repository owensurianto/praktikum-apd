import os
from data import user
from admin import admin_menu
from user import user_menu

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in user and user[username]["password"] == password:
        os.system("cls")
        print(f"Login berhasil! Selamat datang, {username}\n")

        if username == "admin":
            admin_menu()
        else:
            user_menu()
    else:
        os.system("cls")
        print("Login gagal! Username atau password salah.\n")