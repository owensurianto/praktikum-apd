from prettytable import PrettyTable
from data import data_beras, total_penjualan

def hitung_total(harga,jumlah):
    return harga * jumlah

def user_menu():
    global total_penjualan

    while True:
        print("\n=== MENU USER ===")
        print("1. Lihat Stok Beras")
        print("2. Beli Beras")
        print("3. Logout")
        try:
            pilih = int(input("Pilih : "))
            if pilih == 1:
                table = PrettyTable()
                table.field_names = ["No", "Merk", "Harga", "Stok"]
                no = 1
                for m, info in data_beras.items():
                    table.add_row([no, m, info["harga"], info["stok"]])
                    no += 1
                print(table)

            elif pilih == 2:
                table = PrettyTable()
                table.field_names = ["No", "Merk", "Harga", "Stok"]
                daftar = list(data_beras.keys())

                for i,merk in enumerate(daftar):
                    info = data_beras[merk]
                    table.add_row([i+1, merk, info["harga"], info["stok"]])
                print(table)

                pilih_beras = int(input("Pilih No : ")) - 1
                
                if 0 <= pilih_beras < len(daftar):
                    merk = daftar[pilih_beras]
                    jumlah = int(input("Jumlah (Kg): "))

                    if jumlah <= data_beras[merk]["stok"]:
                        total = hitung_total(data_beras[merk]["harga"],jumlah)
                        data_beras[merk]["stok"] -= jumlah
                        total_penjualan += total

                        struk = PrettyTable()
                        struk.field_names = ["Barang","Isi"]
                        struk.add_row(["Nama Beras", merk])
                        struk.add_row(["Harga/Kg", f"Rp{data_beras[merk]['harga']:,}"])
                        struk.add_row(["Jumlah", f"{jumlah} Kg"])
                        struk.add_row(["Total Bayar", f"Rp{total:,}"])

                        print("\n=== STRUK PEMBELIAN ===")
                        print(struk)
                        print("Terima kasih!\n")
            elif pilih == 3:
                break
        except ValueError:
            print("Input harus angka!")