import os

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

total_penjualan = 0

def tampilkan_header(judul):
    print("=" * 35)
    print(f"|  {judul:^29}  |")
    print("=" * 35)

def tampilkan_data_beras():
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

def hitung_total(harga, jumlah):
    return harga * jumlah

def tampilkan_total_penjualan():
    print(f"\nTotal penjualan saat ini: Rp{total_penjualan:,}\n")

while True:
    print("Pilih opsi:")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1":
        username = input("Buat username: ")
        password = input("Buat password: ")
        os.system("cls")
        if username in user:
            print("Username sudah ada, coba yang lain!\n")
        else:
            user[username] = {"password": password}
            print(f"Pengguna {username} berhasil didaftarkan!\n")
    elif pilihan == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username in user and user[username]["password"] == password:
            os.system("cls")
            print(f"Login berhasil! Selamat datang, {username}\n")
            if username == "admin":
                judul = "TOKO BERAS SUMBER REZEKI"
                tampilkan_header(judul)
                menu_admin = {
                    1: "TAMBAH MERK",
                    2: "TAMPILKAN STOK BERAS",
                    3: "UBAH HARGA/STOK",
                    4: "HAPUS STOK",
                    5: "LIHAT TOTAL PENJUALAN",
                    6: "KELUAR"
                }
                for key, value in menu_admin.items():
                    print(f"|  {key}. {value:<26} |")
                print("=" * 35)

                while True:
                    try:
                        pilih = int(input("PILIH : "))
                        if pilih == 1:
                            merk = input("MERK : ")
                            harga = int(input("Harga Beras/KG : "))
                            stok = int(input("Jumlah Stok : "))
                            data_beras[merk] = {"harga": harga, "stok": stok}
                            print("Data berhasil ditambahkan!\n")

                        elif pilih == 2:
                            tampilkan_data_beras()

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

                        elif pilih == 4:
                            merk_hapus = input("Merk Beras yang ingin dihapus: ")
                            if merk_hapus in data_beras:
                                del data_beras[merk_hapus]
                                print(f"Merk '{merk_hapus}' telah dihapus!\n")
                            else:
                                print("Merk tidak ditemukan!\n")

                        elif pilih == 5:
                            tampilkan_total_penjualan()
                            
                        elif pilih == 6:
                            print("Terima kasih, Anda ter-logout!\n")
                            break
                        else:
                            print("Pilihan tidak ada!\n")
                    except ValueError:
                        print("Input harus berupa angka!\n")
            else:
                judul = "TOKO BERAS SUMBER REZEKI"
                tampilkan_header(judul)
                menu_user = {
                    1: "LIHAT STOK BERAS",
                    2: "BELI BERAS",
                    3: "KELUAR"
                }
                for key, value in menu_user.items():
                    print(f"|  {key}. {value:<26} |")
                print("=" * 35)

                while True:
                    try:
                        pilih = int(input("PILIH : "))
                        
                        if pilih == 1:
                            tampilkan_data_beras()
                        
                        elif pilih == 2:
                            if len(data_beras) == 0:
                                print("Stok beras kosong!\n")
                            else:
                                tampilkan_data_beras()
                                try:
                                    pilih_beras = int(input("Pilih nomor beras: ")) - 1
                                    daftar = list(data_beras.keys())
                                    if 0 <= pilih_beras < len(daftar):
                                        merk = daftar[pilih_beras]
                                        jumlah = int(input("Jumlah (kg): "))
                                        harga_beras = data_beras[merk]["harga"]
                                        stok_tersedia = data_beras[merk]["stok"]

                                        if jumlah <= stok_tersedia:
                                            total = hitung_total(harga_beras, jumlah)
                                            data_beras[merk]["stok"] -= jumlah
                                            total_penjualan += total
                                            print("\n===============================")
                                            print("         STRUK PEMBELIAN        ")
                                            print("===============================")
                                            print(f"Nama Beras : {merk}")
                                            print(f"Harga/Kg   : Rp{harga_beras:,}")
                                            print(f"Jumlah     : {jumlah} kg")
                                            print(f"Total Bayar: Rp{total:,}")
                                            print("===============================")
                                            print("Terima kasih telah berbelanja!\n")
                                        else:
                                            print("Stok tidak cukup!\n")
                                    else:
                                        print("Pilihan tidak sesuai!\n")
                                except ValueError:
                                    print("Input harus berupa angka!\n")

                        elif pilih == 3:
                            print("Anda telah keluar.\n")
                            break
                        else:
                            print("Pilihan tidak sesuai!\n")
                    except ValueError:
                        print("Input harus berupa angka!\n")
        else:
            os.system("cls")
            print("Login gagal! Username atau password salah.\n")

    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak ada!\n")
