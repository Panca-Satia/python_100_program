# Menentukan barang tersedia
# created by Panca
# 29-10-2024

print('\n')
print('='*26)
print('Menentukan barang tersedia')
print('='*26)

nama_barang = str(input('Masukan Barang : '))
jumlah_barang = int(input('Masukan Jumlah Barang : '))
harga = int(input('Masukan Harga Barang : '))
ketersediaan_barang = str(input('Apakah barangnya ada? '))


print('Nama Barang : ', nama_barang)
print('Jumlah Barang :', jumlah_barang)
print('Harga Barang : ', harga)

if ketersediaan_barang == "ada":
    print('Ketersediaan : true')
elif ketersediaan_barang == "kosong":
    print('Ketersediaan : false')