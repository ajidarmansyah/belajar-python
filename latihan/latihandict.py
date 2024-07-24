
data_input = {}

print("===== PROGRAM DATABASE =====")
while True:
    key = input("masukan key yang anda inginkan: ")
    value = input("masukan value: ")

    data_input.update({key : value})

    isLanjut = input("ketik y untuk lanjut, \nketik n untuk keluar, \nketik s untuk tampilkan data: ")

    if(isLanjut == "n" or isLanjut == "N"):
        break
    elif (isLanjut == "y" or isLanjut == "Y"):
        continue
    elif (isLanjut == "s" or isLanjut == "S"):
        print(f"{'key':<10} {'value':<20}")
        print("-"*40)
        for key,value in data_input.items():
            print(f"{key:<10} {value:<20}")
        break