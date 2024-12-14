# ini adalah program menampilkan bulan lengkap 
# dibuat pada 24/10/2024
# dibuat oleh Panca
import calendar
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENAMPILKAN BULAN")
print(30*"\033[92m=")

while True:
    try:
        tahun = int(input("masukan tahun (angka):"))
        bulan = int(input("masukan bulan (angka):"))
        print()
        print(f"hasil\n{calendar.month(tahun,bulan)}") 
        while True:
            isdone = str(input("apakah masih mau lagi (mauu/tidak) ? = "))
            if isdone == "mauu":
                break
            elif isdone == "tidak":
                print("TERIMA KASIH")
                exit()
            else:
                print("hanya masukan (mauu / tidak) !")
                break
    except ValueError:
        print("inputan anda tidak valid")
        print("silahkan masukan bilangan bulat")
        break
print("TERIMA KASIH")