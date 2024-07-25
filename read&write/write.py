# menuliskan file eksternal

# mode write akan menimpa 
with open("read&write/data2.txt", mode="w", encoding="utf-8") as file:
    file.write("ini adalah file data2.txt\n")
    file.write("ini adalah baris baru\n")

# mode appand tidak akan menimpa tetapi menambahkan
with open("read&write/data2.txt", mode="a", encoding="utf-8") as file:
    file.write("ini adalah baris baru menggunakan appand")
