# Menghitung frekuensi getaran
# Created by Panca
# 14-12-2024

print('\n')
print('='*30)
print('\tMenghitung frekuensi getaran')
print('='*30)
print()

t = int(input('Masukan lama waktu : '))
n = int(input('Masukan jumlah getaran : '))
F = lambda t, n : n / t

print('Frekuensi getaran adalah : ', F(t,n), 'Hz')
print()