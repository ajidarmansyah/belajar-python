data_dict = {
    'key' : 'value',
    'name' : 'dudung',
    'umur' : 18,
    'alamat' : 'sadeng kulon',
    'teman' : ['ahmad', 'rijal']
}

# akses data dictionary menggunakan key
print(data_dict['name'])
print(data_dict['umur'])
print(data_dict['alamat'])
print(data_dict['teman'])

# akses data menggunakan method get
# pesan error default none
print(data_dict.get('name', 'data key tidak ditemukan'))

# panjang data
LENDATA = len(data_dict)
print(f"panjang data dict {LENDATA}")

# cek key ada atau tidak
KEY = 'kota'
ISKEY = KEY in data_dict
if ISKEY == True:
    print(f"key data {KEY} ditemukan")
else :
    print(f"key data {KEY} tidak ditemukan")

# update data/manipulasi data
data_dict['umur'] = 20

data_dict.update({'kota' : 'Bogor'})
print(data_dict)