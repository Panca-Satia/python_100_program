# menetukan jarak
# Dibuat oleh Panca
# 14-11-2024

print('='*30)
print('Menentukan jarak tempuh')
print('='*30)

jarak = float(input('\nMasukan jarak tempuh dengan satuan cm : '))

kilometer = jarak // 10000
sisa_jarak = jarak % 10000

meter = jarak // 100
sisa_jarak = sisa_jarak % 100

cm = jarak
sisa_jarak = sisa_jarak % jarak

print('Jarak tempuh semut adalah : ', kilometer, 'km,', meter, 'm,', cm, 'cm\n')