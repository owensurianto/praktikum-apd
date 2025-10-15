import os
os.system("cls")
user = {
    "admin": {"password": "admin123"},
    "udin": {"password": "udinsedunia"},
}  
data_beras = [
    ["Lele", 14000, 500],
    ["Berlian", 13500, 200],
    ["Anak Raja", 16000, 150],
    ["Bulog", 9000, 75],
]
while True:
    print("Pilih opsi:")
    print("1. Register") 
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")
    if pilihan == '1': 
        username = input("Buat username: ")
        password = input("Buat password: ")
        os.system("cls")
        if username in user:
            print("Username sudah ada, coba yang lain!")    
        else:
            user[username] = {"password": password}
            print(f"Pengguna {username} berhasil didaftarkan!")
    elif pilihan == "2": 
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username in user and user[username]["password"] == password:
            os.system("cls")
            print(f"Login berhasil! Selamat datang, {username}")
            if username == "admin":
                judul = "TOKO BERAS SUMBER REZEKI"
                menu_admin = [
                    "1. TAMBAH MERK",
                    "2. TAMPILKAN STOK BERAS",
                    "3. UBAH HARGA",
                    "4. HAPUS STOK",
                    "5. KELUAR"
                ]
                print("=" * 35)
                print(f"|  {judul:^29}  |")
                print("=" * 35)
                for item in menu_admin:
                    print(f"|    {item:<28} |")
                print("=" * 35)
                while True:
                    pilih = int(input("PILIH : "))
                    if pilih == 1: 
                        merk = input("MERK : ")
                        harga = int(input("Harga Beras/KG : "))
                        stock = int(input("Jumlah Stock : "))
                        data_beras.append([merk, harga, stock])
                        print("Data berhasil ditambahkan!")
                    elif pilih == 2:
                        if len(data_beras) == 0:
                            print("Stok beras masih kosong.")
                        else:
                            print("="*45)
                            print(f"{'No':<5} {'Merk':<15} {'Harga':<10} {'Stok':<10}")
                            print("="*45)
                            for i in range(len(data_beras)):
                                print(f"{i+1:<5} {data_beras[i][0]:<15} {data_beras[i][1]:<10} {data_beras[i][2]:<10}")
                            print("="*45)
                    elif pilih == 3:
                        merk_beras = input("Merk Beras yang ingin diubah: ")
                        for i in range(len(data_beras)):
                            if data_beras[i][0] == merk_beras:
                                harga_baru = input("Harga/KG: ")
                                stock_baru = input("Jumlah Stok Sekarang: ")
                                data_beras[i][1] = int(harga_baru)
                                data_beras[i][2] = int(stock_baru)
                                print(f"Data Beras {merk_beras} telah diubah!!")
                                break
                        else:
                            print("Merk beras ini tidak ada")
                    elif pilih == 4:
                        merk_lama = input("Merk Beras yang ingin dihapus: ")
                        for i in range(len(data_beras)):
                            if data_beras[i][0] == merk_lama:
                                del data_beras[i]
                                print(f"Merk Beras {merk_lama} Telah dihapus!!")
                                break
                        else:
                            print("Merk beras ini tidak ada")
                    elif pilih == 5:
                        print("Terima kasih Sudah berkunjung, Anda ter-logout!!")
                        break
                    else:
                        print("Pilihan Tidak Ada!!")
            else:
                judul = "TOKO BERAS SUMBER REZEKI"
                menu_perintah = ["1. LIHAT STOK BERAS", "2. BELI BERAS", "3. KELUAR"]
                print("="*35)  
                print(f"|  {judul:^29}  |")
                print("="*35)
                for perintah in menu_perintah:
                    print(f"| {perintah:<32} |")
                print("="*35)
                while True:
                    pilih = int(input("Pilih: "))
                    if pilih == 1:
                        if len(data_beras) == 0:
                            print("Mohon maaf stok beras sedang kosong")
                        else:
                            print("="*45)
                            print(f"{'No':<5} {'Merk':<15} {'Harga':<10} {'Stok':<10}")
                            print("="*45)
                            for i in range(len(data_beras)):
                                print(f"{i+1:<5} {data_beras[i][0]:<15} {data_beras[i][1]:<10} {data_beras[i][2]:<10}")
                            print("="*45)
                    elif pilih == 2:
                        if len(data_beras) == 0:
                            print("Mohon maaf stok beras sedang kosong")
                        else:
                            pilih_beras = int(input("Masukkan nomor beras: ")) - 1
                            if 0 <= pilih_beras < len(data_beras):
                                jumlah_beli = int(input("Jumlah yang ingin dibeli (kg): "))
                                if jumlah_beli <= data_beras[pilih_beras][2]:
                                    total = data_beras[pilih_beras][1] * jumlah_beli
                                    data_beras[pilih_beras][2] -= jumlah_beli
                                    print(f"Anda membeli {jumlah_beli} kg beras {data_beras[pilih_beras][0]}")
                                    print(f"Total harga: Rp{total:,}")
                                    print("Terima kasih telah berbelanja!\n")
                                else:
                                    print("stok tidak cukup!!")
                            else:
                                print("Pilihan tak sesuai!\n")
                    elif pilih == 3:
                        print("Anda telah keluar, Anda Ter-logout\n")
                        break
                    else:
                        print("Pilihan tidak sesuai\n")
        else:
            os.system("cls")
            print("Login gagal! Username atau password salah.")
    else:
        exit()