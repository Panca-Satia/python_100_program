# program menghitung menggunakan eval
# created by Panca
# 12-12-2024
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG MENGGUNAKAN EVAL")
print(30*"\033[92m=")
print()
print("""contoh penggunaan
- 1 + 2
- 5 - 2
- 6 * 5
- 9 / 3
- 5 ** 2
- 10 % 7
            """)
inputan_user = input("hitung sendiri = ")
hasil = eval(inputan_user)
print(f"hasil nya adalah = {hasil}")