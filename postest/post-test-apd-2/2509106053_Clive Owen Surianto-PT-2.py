# Data suhu Celcius
suhu = [27, 33, 46, 55, 67, 92]

# Konversi suhu

# suhu_1 dan suhu_2 ke Fahrenheit
suhu_1 = (suhu[0] * 9/5) + 32
suhu_2 = (suhu[1] * 9/5) + 32

# suhu_3 dan suhu_4 ke Kelvin
suhu_3 = suhu[2] + 273.15
suhu_4 = suhu[3] + 273.15

# suhu_5 dan suhu_6 ke Reamur
suhu_5 = suhu[4] * 4/5
suhu_6 = suhu[5] * 4/5

# Jumlah semua hasil konversi
jumlah = suhu_1 + suhu_2 + suhu_3 + suhu_4 + suhu_5 + suhu_6

# Rata-rata
rata2 = jumlah / len(suhu)

# Variabel NIM
NIM = 53

# Boolean NIM < rata-rata
Bolean = NIM < rata2

# Output
print("Suhu dalam list:", suhu)
print("Konversi suhu_1 (F):", suhu_1)
print("Konversi suhu_2 (F):", suhu_2)
print("Konversi suhu_3 (K):", suhu_3)
print("Konversi suhu_4 (K):", suhu_4)
print("Konversi suhu_5 (R):", suhu_5)
print("Konversi suhu_6 (R):", suhu_6)
print("Jumlah:", jumlah)
print("Rata-rata:", rata2)
print("NIM:", NIM)
print("Bolean (NIM < rata2):", Bolean)
print("Slice index negatif (46-92):", suhu[-4:])
