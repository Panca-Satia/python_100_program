# Toko buku
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Toko buku')
print('='*30)

HARGA_IPHONE = 15000
HARGA_KULKAS = 10000
HARGA_KIPAS = 6000
HARGA_ANDROID = 14000
HARGA_AC = 13000
HARGA_LAPTOP = 20000

iphone = int(input('Masukan jumlah IPHONE : '))
kulkas = int(input('Masukan jumlah Kulkas : '))
kipas = int(input('Masukan jumlah kipas : '))
Android = int(input('Masukan jumlah Android : '))
ac = int(input('Masukan jumlah AC : '))
laptop = int(input('Masukan jumlah laptop : '))

ttl_iphone = iphone * HARGA_IPHONE
ttl_kulkas = kulkas * HARGA_KULKAS
ttl_kipas = kipas * HARGA_KIPAS
ttl_android = Android * HARGA_ANDROID
ttl_AC = ac * HARGA_AC
ttl_laptop = laptop * HARGA_LAPTOP

total = ttl_iphone + ttl_kulkas + ttl_kipas + ttl_android + ttl_AC + ttl_laptop
diskon = total * 12.5/100
bayar = total - diskon


print('Jumlah : ', total)
print('diskon : ', diskon)
print('Total : ', bayar, '\n')