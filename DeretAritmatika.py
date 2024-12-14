# rumus deret aritmatika
# created by Panca
# 12-12-2024

print('\n')
print('='*80)
print('Rumus deret aritmatika menggunakan suku pertama (a) dan suku ke-n (Un)')
print('='*80)

n = int(input('Masukan banyak suku yang dijumlahkan (n) : '))
a = int(input('Masukan suku pertama (a) : '))
Un = int(input('Masukan suku ke-n (Un) : '))

Sn = n/2 * (a + Un)

print('Hasil hitungan deret aritmatika adalah : ', Sn)