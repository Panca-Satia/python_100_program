# menghitung hasil ujian siswa
# 22-11-24
# create by panca
import os
os.system("cls")
print(30 * "\033[94m=")  
print("\033[94mPROGRAM MENGHITUNG HASIL UJIAN SISWA\033[0m") 
print(30 * "\033[94m=")

nilai_siswa = []
mata_ujian = [
    "b.indonesia",
    "b.sunda",
    "b.inggris",
    "ipas",
    "pancasila",
    "sejarah",
    "pab",
    "seni budaya",
    "Daspro",
    "Informatika"
]

for mata in mata_ujian:
    nilai_siswa.append(float(input(f"Masukkan nilai_siswa {mata} = ")))

total = 0
nilai_terbesar = nilai_siswa[0]
nilai_terkecil = nilai_siswa[0]

for i in nilai_siswa:
    total += i
    if i > nilai_terbesar:
        nilai_terbesar = i
    if i < nilai_terkecil:
        nilai_terkecil = i

print(f"Total nilai anda = {total}")
print(f"Rata-rata nilai anda = {total / len(mata_ujian)}")
print(f"Nilai terbesar anda = {nilai_terbesar}")
print(f"Nilai terkecil anda = {nilai_terkecil}")