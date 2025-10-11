# ulangi = 10
# for i in range (ulangi):
#     print(f'Perulangan ke {i}')

# Variabel ulangi digunakan untuk menentukan banyaknya perulangan
# Variabel i berfungsi untuk menampung indeks (perulangan ke berapa)
# Fungsi range(parameter) berfungsi untuk menentukan jangkauan sesuai dengan
# isi yang berada pada parameter-1

# PERULANGAN FOR LIST
# simpan = [1, 'Dapupu', 4.00, True]
# for i in simpan:
#     print(i)
# b1=["ajis","Mujahit","Tian"]
# print(b1)
# for i in b1:
#     print(f"isi fari list adalah ", i)

# for i in range (8):
#     for j in range (i+1):
#         print("*", end=" ")
#     print()

# for i in range(1, 4):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 5):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}', end=" ")
#     print('') #biar ada jarak tiap iterasi

# dompet = [1000,2000,3000,4000]
# for uang in range (len(dompet)):
#     print(dompet[uang])

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#         hitung += 1
#         jawab = input("Ulang lagi? ")
# print(f"Total perulangan: {hitung}")
# username = input("Masukan usn:")
# while username == "":
#     username = input("Masukan usn:")

angka = [2, 5, 8, 12, 15, 7, 20]
print("Mencari angka pertama yang lebih besar dari 10...")
for n in angka:
    print(f"Sekarang memeriksa angka: {n}")
    if n > 10:
        print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
        break
print("Program selesai.")