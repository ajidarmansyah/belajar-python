# looping dictionary
data_dict = {
    'key' : 'value',
    'name' : 'dudung',
    'umur' : 18,
    'alamat' : 'sadeng kulon'
}

# hanya mengambil key nya saja
for data in data_dict:
    print(data)

print('\n')
# cara mengambil key pada dictionary
for key in data_dict.keys():
    print(data_dict.get(key))

print('\n')
# cara mengambil value pada dictionary
for value in data_dict.values():
    print(value)

print('\n')
# cara mengambil key dan value pada dictionary
for key,value in data_dict.items():
    print(f"key = {key} value {value}")
