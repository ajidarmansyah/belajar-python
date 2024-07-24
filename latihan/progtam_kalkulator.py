
print("===== PROGARAM KALKULATOR SEDERHANA =====")
input_data1 = int(input("Angka pertama :"))
input_operasi = input("Pilih operasi +,-,x,/ :")
input_data2 = int(input("Angka kedua :"))

if input_operasi == "+":
    hasil = input_data1 + input_data2
    print(f"Hasil perhitungan = {hasil}")
elif input_operasi == "-":
    hasil = input_data1 - input_data2
    print(f"Hasil perhitungan = {hasil}")
elif input_operasi == "x":
    hasil = input_data1 * input_data2
    print(f"Hasil perhitungan = {hasil}")
elif input_operasi == "/":
    hasil = input_data1 / input_data2
    print(f"Hasil perhitungan = {hasil}")

print("Program berakhir")