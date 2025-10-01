# username dan pw yang benar
username_ril = "Owen"
password_ril = "053"

# form login
print("~~~~LOGIN~~~~")
username = input("Masukan Username Anda: ")
password = input("Masukan Password Anda: ")
if username_ril == username and password_ril == password:
    print("Login berhasil!")
else:
    print("Username atau Password salah!")
    exit()

# Menu Kalkulator Multifungsi
print("\n--- Kalkulator Multifungsi ---")
print("1. Konversi panjang")
print("2. Konversi Massa")
print("3. Konversi suhu")
print("4. Konversi Waktu")
print("5. Konversi Mata Uang")
# Konversi panjang
pilihan = int(input("Pilih Kalkulator yang ingin digunakan: "))
if pilihan == 1:
    print("\n--- Konversi Panjang ---")
    print("1. Kaki (feet) -> Meter")
    print("2. Kilometer -> Meter")
    print("3. Centimeter -> Meter")
    pilih = int(input("Pilih Konversi yang diinginkan: "))
    if pilih == 1:
        feet = float(input("Masukan nilai feet: "))
        meter = feet * 0.3048
        print(f"{feet} feet = {meter} Meter")
    elif pilih == 2:
        km = float(input("Masukkan nilai (km): "))
        meter = km * 1000
        print(f"{km} km = {meter} meter")
    elif pilih == 3:
        cm = float(input("Masukkan nilai (cm): "))
        meter = cm / 100
        print(f"{cm} cm = {meter} meter")
    else:
        print("Pilihan tidak sesuai!")

# konversi massa
elif pilihan == 2:
    print("\n--- Konversi Massa ---")
    print("1. Pon (pound) -> Kilogram")
    print("2. Ton -> Kilogram")
    print("3. Gram -> Kilogram")
    print("4. Ons -> Kilogram")
    print("5. Miligram -> Kilogram")
    pilih = int(input("Pilih konversi: "))
    if pilih == 1:
        pound = float(input("Masukkan nilai (pound): "))
        kg = pound * 0.453592
        print(f"{pound} pound = {kg} kg")
    elif pilih == 2:
        ton = float(input("Masukkan nilai (ton): "))
        kg = ton * 1000
        print(f"{ton} ton = {kg} kg")
    elif pilih == 3:
        gram = float(input("Masukkan nilai (gram): "))
        kg = gram / 1000
        print(f"{gram} gram = {kg} kg")
    elif pilih == 4:
        ons = float(input("Masukkan nilai (ons): "))
        kg = ons * 0.1
        print(f"{ons} ons = {kg} kg")
    elif pilih == 5:
        mg = float(input("Masukkan nilai (mg): "))
        kg = mg / 1000000
        print(f"{mg} mg = {kg} kg")
    else:
        print("Pilihan tidak sesuai!")

# Konversi suhu
elif pilihan == 3:
    print("\n--- Konversi Suhu ---")
    print("1. Celcius -> Kelvin")
    print("2. Fahrenheit -> Kelvin")
    print("3. Reamur -> Kelvin")
    pilih = int(input("Pilih konversi: "))
    if pilih == 1:
        c = float(input("Masukkan suhu (°C): "))
        k = c + 273.15
        print(f"{c} °C = {k} K")
    elif pilih == 2:
        f = float(input("Masukkan suhu (°F): "))
        k = (f - 32) * 5/9 + 273.15
        print(f"{f} °F = {k} K")
    elif pilih == 3:
        r = float(input("Masukkan suhu (°Re): "))
        k = r * 5/4 + 273.15
        print(f"{r} °Re = {k} K")
    else:
        print("Pilihan tidak sesuai!")

# Konversi Waktu
elif pilihan == 4:
    print("\n--- Konversi Waktu ---")
    print("1. Menit -> Detik")
    print("2. Jam -> Detik")
    pilih = int(input("Pilih Konversi: "))
    if pilih == 1:
        menit = float(input("Masukkan nilai (menit): "))
        detik = menit * 60
        print(f"{menit} menit = {detik} detik")
    elif pilih == 2:
        jam = float(input("Masukkan nilai (jam): "))
        detik = jam * 3600
        print(f"{jam} jam = {detik} detik")
    else:
        print("Pilihan tidak sesuai!")

# Konversi Mata Uang
elif pilihan == 5:
    print("\n--- Konversi mata uang ---")
    print("1. Rupiah -> Dolar")
    print("2. Dolar -> Rupiah")
    print("3. Rupiah -> Yen")
    print("4. Yen -> Rupiah")
    print("5. Rupiah -> Euro")
    print("6. Euro -> Rupiah")
    pilih = int(input("Pilih konversi: "))
    if pilih == 1:
        rp = float(input("Masukkan Rupiah: "))
        usd = rp / 16649
        print(f"{rp} IDR = {usd} USD")
    elif pilih == 2:
        usd = float(input("Masukkan Dolar: "))
        rp = usd * 16649
        print(f"{usd} USD = {rp} IDR")
    elif pilih == 3:
        rp = float(input("Masukkan Rupiah: "))
        yen = rp / 113
        print(f"{rp} IDR = {yen} JPY")
    elif pilih == 4:
        yen = float(input("Masukkan Yen: "))
        rp = yen * 113
        print(f"{yen} JPY = {rp} IDR")
    elif pilih == 5:
        rp = float(input("Masukkan Rupiah: "))
        eur = rp / 19500
        print(f"{rp} IDR = {eur} EUR")
    elif pilih == 6:
        eur = float(input("Masukkan Euro: "))
        rp = eur * 19500
        print(f"{eur} EUR = {rp} IDR")
    else:
        print("Pilihan tidak Sesuai!")
else:
    print("Pilihan Tidak Sesuai!")
