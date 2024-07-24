# method list untuk merubah nilai

daftar_buah = ["apel", "jeruk", "pisang", "jambu"]
daftar_sayur = ["sawi", "bayam", "brokoli"]

# menambahkan nilai
daftar_sayur.append("lobak")
print(daftar_sayur)

# menghapus nilai
daftar_buah.pop(1)
print(daftar_buah)

# menggabung nilai list
daftar_buah.extend(daftar_sayur)
print(daftar_buah)

# menduplikat list
a = daftar_buah.copy()
print(a)