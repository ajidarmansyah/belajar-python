# fungsi input hanya dapat mengembalikan string
data = input('Masukan data: ')

# jika ingin variable data berisi integer atau float, harus di casting
data2 = int(input('Masukan data number: '))

data3 = float(input('Masukan data desimal: '))

# untuk boolean harus dicesting ke integer untuk mendapatkan nilai 0 atau 1
data4 = bool(int(input('Masukan data 0/1: ')))

print(data, "Tipe : ", type(data))
print(data2, "Tipe : ", type(data2))
print(data3, "Tipe : ", type(data3))
print(data4, "Tipe : ", type(data4))