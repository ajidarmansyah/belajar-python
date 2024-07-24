# data base
data = {}

# menu
print("=== PROGRAM DATA BASE ===")
print("1. Input data")
print("2. Update data")
print("3. Delete data")
print("4. Tampilkan data")

while True:
    pilih_menu = int(input("PILIH NOMOR: "))
    if(pilih_menu == 1):
        input_kode_barang = input("Masukan kode barang: ")
        input_nama_barang = input("Masukan nama barang: ")

        data.update({input_kode_barang:input_nama_barang})

        isLanjut = input("lanjut? y/n: ")
        if(isLanjut == 'y' or isLanjut == 'Y'):
            continue
        elif(isLanjut == 'n' or isLanjut == 'N'):
            break
        else:
            print("pilih y untuk yes dan n untuk no")
    if(pilih_menu == 2):
        pilih_kode_barang = input("Masukan kode barang: ")
        ubah_nama_barang = input("Masukan nama barang: ")

        data.update({pilih_kode_barang:ubah_nama_barang})

        isLanjut = input("lanjut? y/n: ")
        if(isLanjut == 'y' or isLanjut == 'Y'):
            continue
        elif(isLanjut == 'n' or isLanjut == 'N'):
            break
        else:
            print("pilih y untuk yes dan n untuk no")
    if(pilih_menu == 3):
        input_delete_data = input("Pilih kode barang yang ingin dihapus: ")
        data.pop(input_delete_data)

        isLanjut = input("lanjut? y/n: ")
        if(isLanjut == 'y' or isLanjut == 'Y'):
            continue
        elif(isLanjut == 'n' or isLanjut == 'N'):
            break
        else:
            print("pilih y untuk yes dan n untuk no")
    if(pilih_menu == 4):
        print(f"{'KODE BARANG':<20} {'NAMA BARANG':<30}")
        print('-'*50)
        for kode,barang in data.items():
            print(f"{kode:<20} {barang:<30}")
            