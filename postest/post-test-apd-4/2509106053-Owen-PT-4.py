# Login
while True:
    username = input("Masukkan username: ")
    password = input("Masukkan password (3 digit NIM terakhir): ")

    if username == "Owen" and password == "053":
        print("Login berhasil!\n")
        break
    else:
        print("Username atau password salah, coba lagi!\n")

# VARIABEL UNTUK NILAI AWAL
total_a = 0
total_b = 0
total_ab = 0
total_o = 0
# Input Golongan darah A,B,AB DAN O
while True:
    golongan = input("Masukkan golongan darah anda(A/B/AB/O): ")
    if golongan == "A":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "+":
            print("Golongan darah anda: A+")
        else:
            print("Golongan darah anda: A-")
        jumlah = int(input("Masukkan jumlah kantong darah: "))
        total_a += jumlah * 500

    elif golongan == "B":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "+":
            print("Golongan darah anda: B+")
        else:
            print("Golongan darah anda: B-")
        jumlah = int(input("Masukkan jumlah kantong darah: "))
        total_b += jumlah * 500

    elif golongan == "AB":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "+":
            print("Golongan darah anda: AB+")
        else:
            print("Golongan darah anda: AB-")
        jumlah = int(input("Masukkan jumlah kantong darah: "))
        total_ab += jumlah * 500

    elif golongan == "O":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "+":
            print("Golongan darah anda: O+")
        else:
            print("Golongan darah anda: O-")
        jumlah = int(input("Masukkan jumlah kantong darah: "))
        total_o += jumlah * 500

    else:
        print("Golongan darah tidak dikenal!")
        continue
# 4. pertanyaan apakah mau input lagi
    ulang = input("Apakah anda masih mau input lagi (Y/T)? ")
    if ulang == "T":
        break
    print()
    # 5. OUTPUT RINGKASAN
print("\n==== RINGKASAN JUMLAH DARAH ====")
print(f"Total darah A  : {total_a} ml")
print(f"Total darah B  : {total_b} ml")
print(f"Total darah AB : {total_ab} ml")
print(f"Total darah O  : {total_o} ml")
print("=================================")