def tambah(*args: float) -> float:
    hasil = 0
    for angka in args:
        hasil += angka

    return hasil

def kali(*args: float) -> float:
    hasil = 1
    for angka in args:
        hasil *= angka

    return hasil

def pangkat(n):
    return lambda angka:angka**n
