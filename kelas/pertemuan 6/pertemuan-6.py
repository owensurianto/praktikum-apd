# # # # # list_mahasiswa = ["andi","Budi", "Citra", "Dewi"]
# # # # # print("Nama anda", list_mahasiswa[0])

# # # # # set_makanan = {"nasi","nasi", "ayam", "ayam", "buah"}
# # # # # set_makanan2 = {"nasi", "ayam"}
# # # # # set_minuman = {"air", "jus","susu","teh"}
# # # # # setall = set_makanan.union(set_minuman)
# # # # # print(setall)
# # # # # abc = set_makanan.intersection(set_makanan2)
# # # # # cba = set_makanan.difference(set_makanan2)
# # # # # print(cba)
# # # # # print(abc)
# # # # # list_makanan = set_makanan
# # # # # print("makanan favorit saya adalah ", list_makanan)
# # # # # for minum in set_minuman:
# # # # #     print(f"Minuman fav saya adalah {minum}")

# # # # # set_minuman.discard("air")
# # # # # print(set_minuman)
# # # # # Daftar_buku = {
# # # # # "Buku1" : "Bumi Manusia",
# # # # # "Buku2" : "Laut Bercerita"
# # # # # }
# # # # # print(Daftar_buku["Buku1"])
# # # # # print(Daftar_buku)
# # # # # Biodata = {
# # # # # "Nama" : "Ananda Daffa Harahap",
# # # # # "NIM" : 2409106050,
# # # # # "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"].
# # # # # "Mahasiswa_Aktif" : True,
# # # # # "Social Media" : {
# # # # #     "Instagram" : "daffahrhap"
# # # # # }
# # # # # }
# # # # Nilai = {
# # # # "Matematika": 80,
# # # # "B. Indonesia": 90,
# # # # "B. Inggris": 81,
# # # # "Kimia": 78,
# # # # "Fisika": 80
# # # # }
# # # # # Tanpa menggunakan items()
# # # # for i in Nilai:
# # # #     print(i)
# # # # print("") # pemisah
# # # # # Menggunakan items()
# # # # for i, j in Nilai.items():
# # # #     print(f"Nilai {i} anda adalah {j}")
# # # Film = {
# # # "Avenger Endgame" : "Action",
# # # "Sherlock Holmes" : "Mystery",
# # # "The Conjuring" : "Horror"
# # # }
# # # #Sebelum Ditambah
# # # print(Film)
# # # Film["Zombieland"] = "Comedy"
# # # Film.update({"Hours" : "Thriller"})
# # # #Setelah Ditambah
# # # print(Film)
# # data = {
# # "Nama" : "Daffa",
# # "Umur" : 19,
# # "Jurusan" : "Informatika"
# # }
# # #Sebelum Dihapus
# # print(data)
# # del data["Nama"]
# # print(data)
# # #memanggil data yang telah dihapus
# # print(data.get("Nama"))
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)
Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
    print("")