print("===== PROGRAM ENKRIPSI SEDERHANA =====")
data = input("Masukan data: ")
data_acuan = "abcdefghijklmnopqrstuvwxyz"

i = 0
data_enkripsi = []
while i < len(data):
    data_baru = data_acuan.find(data[i]) + 5
    # print(data_acuan[data_baru])
    data_enkripsi.append(data_acuan[data_baru])
    i += 1

hasil = " ".join(data_enkripsi)
print(hasil)
