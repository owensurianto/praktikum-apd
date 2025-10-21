import os
os.system("cls")

user = {
    "admin": {"password": "admin123"},
    "udin": {"password": "udinsedunia"},
}
data_beras = {
    "Lele": {"harga": 14000, "stok": 500},
    "Berlian": {"harga": 13500, "stok": 200},
    "Anak Raja": {"harga": 16000, "stok": 150},
    "Bulog": {"harga": 9000, "stok": 75},
}

while True:
    print("Pilih opsi:")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")

    # REGISTER
    if pilihan == "1":
        username = input("Buat username: ")
        password = input("Buat password: ")
        os.system("cls")

        if username in user:
            print("Username sudah ada, coba yang lain!\n")
        else:
            user[username] = {"password": password}
            print(f"Pengguna {username} berhasil didaftarkan!\n")

    # LOGIN
    elif pilihan == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in user and user[username]["password"] == password:
            os.system("cls")
            print(f"Login berhasil! Selamat datang, {username}\n")

            # ================= ADMIN =================
            if username == "admin":
                judul = "TOKO BERAS SUMBER REZEKI"
                menu_admin = {
                    1: "TAMBAH MERK",
                    2: "TAMPILKAN STOK BERAS",
                    3: "UBAH HARGA/STOK",
                    4: "HAPUS STOK",
                    5: "KELUAR"
                }
                print("=" * 35)
                print(f"|  {judul:^29}  |")
                print("=" * 35)
                for key, value in menu_admin.items():
                    print(f"|  {key}. {value:<26} |")
                print("=" * 35)
                while True:
                    pilih = int(input("PILIH : "))
                    # TAMBAH MERK
                    if pilih == 1:
                        merk = input("MERK : ")
                        harga = int(input("Harga Beras/KG : "))
                        stok = int(input("Jumlah Stok : "))
                        data_beras[merk] = {"harga": harga, "stok": stok}
                        print("Data berhasil ditambahkan!\n")
                    # TAMPILKAN STOK
                    elif pilih == 2:
                        if len(data_beras) == 0:
                            print("Stok beras masih kosong.\n")
                        else:
                            print("=" * 45)
                            print(f"{'No':<5}{'Merk':<15}{'Harga':<10}{'Stok':<10}")
                            print("=" * 45)
                            no = 1
                            for merk, info in data_beras.items():
                                print(f"{no:<5}{merk:<15}{info['harga']:<10}{info['stok']:<10}")
                                no += 1
                            print("=" * 45)
                    # UBAH DATA
                    elif pilih == 3:
                        merk_ubah = input("Merk Beras yang ingin diubah: ")
                        if merk_ubah in data_beras:
                            harga_baru = int(input("Harga baru/KG: "))
                            stok_baru = int(input("Jumlah Stok baru: "))
                            data_beras[merk_ubah]["harga"] = harga_baru
                            data_beras[merk_ubah]["stok"] = stok_baru
                            print(f"Data beras '{merk_ubah}' telah diperbarui!\n")
                        else:
                            print("Merk tidak ditemukan!\n")
                    # HAPUS DATA
                    elif pilih == 4:
                        merk_hapus = input("Merk Beras yang ingin dihapus: ")
                        if merk_hapus in data_beras:
                            del data_beras[merk_hapus]
                            print(f"Merk '{merk_hapus}' telah dihapus!\n")
                        else:
                            print("Merk tidak ditemukan!\n")
                    elif pilih == 5:
                        print("Terima kasih, Anda ter-logout!\n")
                        break
                    else:
                        print("Pilihan tidak ada!\n")
            # ================= USER BIASA =================
            else:
                judul = "TOKO BERAS SUMBER REZEKI"
                menu_user = {
                    1: "LIHAT STOK BERAS",
                    2: "BELI BERAS",
                    3: "KELUAR"
                }
                print("=" * 35)
                print(f"|  {judul:^29}  |")
                print("=" * 35)
                for key, value in menu_user.items():
                    print(f"|  {key}. {value:<26} |")
                print("=" * 35)
                while True:
                    pilih = int(input("PILIH : "))
                    # LIHAT STOK
                    if pilih == 1:
                        if len(data_beras) == 0:
                            print("Stok beras kosong!\n")
                        else:
                            print("=" * 45)
                            print(f"{'No':<5}{'Merk':<15}{'Harga':<10}{'Stok':<10}")
                            print("=" * 45)
                            no = 1
                            for merk, info in data_beras.items():
                                print(f"{no:<5}{merk:<15}{info['harga']:<10}{info['stok']:<10}")
                                no += 1
                            print("=" * 45)
                    # BELI BERAS
                    elif pilih == 2:
                        if len(data_beras) == 0:
                            print("Stok beras kosong!\n")
                        else:
                            print("\nDaftar Beras yang Dijual:")
                            print("=" * 45)
                            print(f"{'No':<5}{'Merk':<15}{'Harga':<10}{'Stok':<10}")
                            print("=" * 45)
                            daftar = list(data_beras.keys())
                            for i in range(len(daftar)):
                                merk = daftar[i]
                                info = data_beras[merk]
                                print(f"{i+1:<5}{merk:<15}{info['harga']:<10}{info['stok']:<10}")
                            print("=" * 45)
                            pilih_beras = int(input("Pilih nomor beras: ")) - 1
                            if 0 <= pilih_beras < len(daftar):
                                merk = daftar[pilih_beras]
                                jumlah = int(input("Jumlah (kg): "))
                                if jumlah <= data_beras[merk]["stok"]:
                                    total = jumlah * data_beras[merk]["harga"]
                                    data_beras[merk]["stok"] -= jumlah
                                    print("\n===============================")
                                    print("         STRUK PEMBELIAN        ")
                                    print("===============================")
                                    print(f"Nama Beras : {merk}")
                                    print(f"Harga/Kg   : Rp{data_beras[merk]['harga']:,}")
                                    print(f"Jumlah     : {jumlah} kg")
                                    print(f"Total Bayar: Rp{total:,}")
                                    print("===============================")
                                    print("Terima kasih telah berbelanja!\n")
                                else:
                                    print("Stok tidak cukup!\n")
                            else:
                                print("Pilihan tidak sesuai!\n")
                    elif pilih == 3:
                        print("Anda telah keluar.\n")
                        break
                    else:
                        print("Pilihan tidak sesuai!\n")
        else:
            os.system("cls")
            print("Login gagal! Username atau password salah.\n")
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak ada!\n")