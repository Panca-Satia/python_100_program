# Menentukan pembulatan nilai belanja
# created by Panca
# 12-12-2024

print('\n')
print('='*30)
print('Menentukan pembulatan nilai belanja')
print('='*30)

PEMBAGI = 25
nilai_belanja = int(input('\nMasukan nilai belanja : '))
sisa = nilai_belanja % PEMBAGI
nilai_bulat = nilai_belanja - sisa

print('Nilai belanja yang sudah dibulatkan : Rp.',nilai_bulat)