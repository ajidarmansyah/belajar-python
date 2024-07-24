# method untuk string
# upper(), lower(), strip(), replace(), split()

data_string = "Hello, World"
print(data_string.upper())
print(data_string.lower())

data_string2 = " Hello, World "
print(data_string2.strip())
print(data_string.replace("H", "J"))
print(data_string.split(","))

# format string
# format string bisa juga digunakan didalam function
age = 18
sayHello = f"Hi, may name is aji i'm {18}"
print(sayHello)

# tambah nol dibelakang
price = 12
data = f"Harga barang {price:.3f}"
print(data)

# bisa untuk melakukan perhitungan
data = f"Harga barang {price + 5}"
print(data)

# function untuk menghitung panjang string
print(len(data_string))
