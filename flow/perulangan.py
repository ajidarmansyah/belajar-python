# perulangan
print("======= PERULANGAN =======")
data_range = int(input("Renge data ="))

for i in range(1, data_range + 1):
    if i == 3:
        continue # jika kondisi true maka aksi dibawah akan dilewat
        # pass # tidak akan terjadi apa-apa
    print(i)