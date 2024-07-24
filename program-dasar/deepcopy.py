# teknik menduplikasi list 2D
list_2D = [[1,2],[5,4]]
list_2D_copy = list_2D.copy()

print(f"address list : {hex(id(list_2D))}")
print(f"address list : {hex(id(list_2D_copy))}\n")

# address yang berbeda hanya bagian luar, bagian dalam masih sama
print("data member ke-1")
print(f"address list : {hex(id(list_2D[0]))}")
print(f"address copy : {hex(id(list_2D_copy[0]))}\n")

list_2D[0][0] = 5# cara mengakses dan merubah data pada list 2D
print(f"address list : {list_2D}")
print(f"address copy : {list_2D_copy}\n")

# copy semua list menggunakan deepcopy
from copy import deepcopy

list_2D_deep = deepcopy(list_2D)

list_2D[0][0] = 12
print("merubah nilai menggunakan deepcopy")
print(f"address list : {list_2D}")
print(f"address list : {list_2D_deep}\n")