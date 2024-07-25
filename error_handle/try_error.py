# melakukan pengujian kode menggunakan try
hasil = 0
try:
    input_user = int(input("Masukan bilangan pembagi: "))
    hasil = 10/input_user
except Exception as error_massange:
    print("bilangan tidak bisa dibagi dengan 0")
    print(error_massange)

print(hasil)

# studi kasus
try:
    with open("error_handle/data.txt", mode="r") as file:
        data = file.read()
        print(data)
except:
    with open("error_handle/data.txt", mode="w", encoding="utf-8") as file:
        file.write("file dibuat")
        print("data tidak ditemukan, dan akan dibuat!")

# cara membuat exceptsion
from numbers import Number

def jumlah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harus number"
    return a+b

print(jumlah(5,'v'))