from prettytable import PrettyTable
from data import data_beras, total_penjualan

def admin_menu():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Tambah Merk")
        print("2. Tampilkan Stok Beras")
        print("3. Ubah Harga/Stok")
        print("4. Hapus Stok")
        print("5. Lihat Total Penjualan")
        print("6. Logout")

        try:
            pilih = int(input("Pilih : "))
            if pilih == 1:
                merk = input("Merk : ")
                harga = int(input("Harga : "))
                stok = int(input("Stok : "))
                data_beras[merk] = {"harga": harga, "stok": stok}
                print("Data ditambahkan!\n")

            elif pilih == 2:
                table = PrettyTable()
                table.field_names = ["No", "Merk", "Harga", "Stok"]
                no = 1
                for m, info in data_beras.items():
                    table.add_row([no, m, info["harga"], info["stok"]])
                    no += 1
                print(table)

            elif pilih == 3:
                merk = input("Merk : ")
                if merk in data_beras:
                    harga = int(input("Harga Baru : "))
                    stok = int(input("Stok Baru : "))
                    data_beras[merk]["harga"] = harga
                    data_beras[merk]["stok"] = stok
                else:
                    print("Merk tidak ada!")

            elif pilih == 4:
                merk = input("Merk : ")
                if merk in data_beras:
                    del data_beras[merk]
                else:
                    print("Merk tidak ditemukan!")

            elif pilih == 5:
                print(f"\nTotal Penjualan : Rp{total_penjualan:,}\n")

            elif pilih == 6:
                print("Logout...")
                break

            else:
                print("Pilihan tidak ada!")

        except ValueError:
            print("Input harus angka!")
