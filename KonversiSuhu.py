# Menentukan konversi suhu
# created by Panca
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan konversi suhu')
print('='*30)

celcius = int(input('Masukan suhu (dalam celcius) : '))

reamur = 4/5 * celcius
fahrenheit = 9/5 * celcius + 32
kelvin = 273 + celcius

print('Suhu dalam reamur adalah : ', reamur)
print('Suhu dalam fahrenheit adalah : ', fahrenheit)
print('Suhu dalam kelvin adalah : ', kelvin)