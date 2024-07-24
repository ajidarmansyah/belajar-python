a = 10

def fungsi():
    a = 5
    print(f"ini adalah a didalam fungsi{a}")

if True:
    a = 1
    print(f"ini adalah a didalam kondisi {a}")

print(f"ini adalah a global{a}")
fungsi()