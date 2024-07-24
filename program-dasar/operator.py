# not or and
# bitwise : not(~), and(&&), or(||), xor(^), shift right(<<), shift left(>>)

a = 5
b = 10
c = 5

# not
hasil = not(a < b) # hasil akan berkebalikan
print(hasil)

# and
hasil = a < b and b > a # akan true jika kedua kondisi true dan sebaliknya
print(hasil)

# or
hasil = a > b or b > a # salah satu true akan true
print(hasil)

# is dan is not
hasil = a is c
print(hasil)
hasil = a is not b
print(hasil)

# in dan not in
x = ["apple", "bannana"]
print("bannana" in x)
print("bannana" not in x)