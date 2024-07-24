# membaca file eksternal
print(4*"=", "MEMBACA FILE EKSTERNAL", 4*"=")
file = open("read&write/data.txt", mode="r")

print(f"Apakah file bisa dibaca : {file.readable()}")
print(file.read())
file.close()

# file akan otomatis di colse
print(4*"=", "MEMBACA FILE EKSTERNAL MENGGUNAKAN WIDH", 4*"=")
with open("read&write/data.txt", mode="r") as file:
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")
