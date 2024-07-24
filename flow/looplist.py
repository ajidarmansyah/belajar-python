# looping list
data_list = [1,2,3,4,5]

# looping biasa
for data in data_list:
    print(data)

# enumerate
for index,data in enumerate(data_list):
    print(f"index {index} = {data}")

# list comprehension
data_final = [data**2 for data in data_list]
print(data_final)