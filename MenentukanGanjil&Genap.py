# menentukan ganjil dan genap
# created by Panca
# 31-10-2024

print('\n')
print('='*30)
print('Menentukan ganjil genap')
print('='*30)

angka = int(input("\nMasukkan sebuah angka: "))

sisa = angka % 2

if sisa == 0:
    print(angka, "adalah bilangan genap.")
else:
    print(angka, "adalah bilangan ganjil.")