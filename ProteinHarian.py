# ini merupakan sebuah program menentukan jumlah protein ideal perhari
# Created by Panca
# 8 - 10 - 2024
import os
os.system("cls")
print(35*"\022m=")
print("\022[31mPROGRAM MENENTUKAN JUMLAH PROTEIN  HARIAN".center(40))
print(35*"\022[34m=")

kelamin = str(input("masukan jenis kelamin anda (cowok/cewek) = "))
umur = int(input("masukan umur anda = "))
   
if kelamin == "cowok":
    if 1 <= umur <= 3:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 14 gram") 
    elif 4 <= umur <= 8:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 19 gram") 
    elif 9 <= umur <= 13:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 34 gram") 
    elif 14 <= umur <= 18:
        print("kamu sudah remaja")
        print("protein yang harus kamu konsumsi perhari\n adalah 52 gram") 
    elif 19 <= umur <= 50:
        print("kamu sudah dewasa")
        print("protein yang harus kamu konsumsi perhari\n adalah 56 gram") 
    elif umur < 51:
        print("kamu sudah manula")
        print("protein yang harus kamu konsumsi perhari\n adalah 56 gram") 
elif kelamin == "cewek":
    if 1 <= umur <= 3:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 14 gram") 
    elif 4 <= umur <= 8:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 19 gram") 
    elif 9 <= umur <= 13:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 34 gram") 
    elif 14 <= umur <= 18:
        print("kamu sudah remaja")
        print("protein yang harus kamu konsumsi perhari\n adalah 46 gram") 
    elif 19 <= umur <= 50:
        print("kamu sudah dewasa")
        print("protein yang harus kamu konsumsi perhari\n adalah 46 gram") 
    elif umur < 51:
        print("kamu sudah manula")
        print("protein yang harus kamu konsumsi perhari\n adalah 46 gram")