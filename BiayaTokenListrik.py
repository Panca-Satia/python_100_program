# biaya listrik rumah
# di buat pada 22/10/2024
# created by Panca
import os
os.system("cls")
TARIF = 1500
while True:
    print(30 * "\033[94m=")  
    print("\033[94mPROGRAM MENENTUKAN BIAYA LISTRIK PER BULAN\033[0m") 
    print(30 * "\033[94m=")
    print()
    try:
        bulan_pemakaian = float(input("berapa bulan yang anda inginkan = "))
        daya_listrik = float(input("masukan besar daya (w/watt) = "))
        waktu = float(input("berapa total jam pemakaian per bulan = "))
        biaya_listrik = (daya_listrik / 1000) * waktu * TARIF * 30 * bulan_pemakaian
        print(f"biaya listrik rumah anda selama {bulan_pemakaian} bulan = {biaya_listrik:.2f} ")
        while True:
                isdone = str(input("apakah masih mau lagi (iya/tidak) ? = "))
                if isdone == "iya":
                    break
                elif isdone == "tidak":
                    print("terimakasihh program selesai")
                    exit()
                else:
                    print("Input tidak valid. Silakan masukkan 'iya' untuk iya atau 'tidak' untuk tidak.")    
    except ValueError:
        print("inputan anda tidak valid")
        print("masukan bilangan bulat / float")
        break
print("TERIMA KASIH")

        