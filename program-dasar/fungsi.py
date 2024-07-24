# fungsi dalam python
# def kuadrat(angka):
#     print(angka*angka)

# kuadrat(4)

def hitung_luas_persegi(ankga1, angka2):
    hasil = ankga1 * angka2
    return hasil

print(hitung_luas_persegi(2,5))

# default argument

def hitung_persegi(angka = 0):
    return angka**2

print(hitung_persegi(5))

# type hints

def fungsi_hints(argument:int) -> int:
    hasil = 10**argument
    return hasil

print(fungsi_hints(2))

# fungsi args
# mengembalikan tupels
def tambah(*data_input:int) -> int:
    output = 0
    for angka in data_input:
        output += angka
        
    return output

# fungsi kwargs
# mengembalikan dictionary
def fungsi(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"nama saya {nama}, tinggi {tinggi} dan berat saya {berat}")

fungsi(nama = "ujang", tinggi = 170, berat = 62)

# studi kasus kwargs
def math(*args,**kwargs):
    if kwargs['option'] == 'tambah':
        output = 0
        for angka in args:
            output += angka
    
    if kwargs['option'] == 'kali':
        output = 1
        for angka in args:
            output *= angka
    
    return output

hasil = math(1,2,3,4,option = 'tambah')
print(hasil)
hasil = math(1,2,3,4,option = 'kali')
print(hasil)

# fugsi lambda
kuadrat = lambda angka : angka**2
print(f"fungsi lambda kuadrat {kuadrat(2)}")

# anonymouse function

def pangkat(pangkat):
    return lambda angka : angka**pangkat

pangkat2 = pangkat(2)
print(f"fungsi anonymouse pangkat2 = {pangkat2(4)}")