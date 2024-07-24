# IF dan ELSE staitment

print("=====program pengecekan nomor=====")
data_number = int(input("input nomor : "))

if data_number % 2 == 0:
    print(f"{data_number} adalah bilangan genap")
elif data_number % 2 == 1 :
    print(f"{data_number} adalah bilangan ganjil")
else :
    print("input bukan nomor")
