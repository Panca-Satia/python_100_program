# ini adalah Program menulis hal berulang
# created by panca
# 13-12-2024
import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENULIS BERULANG")
print(30*"\033[92m=")
print()

print(f"apa yang kamu fikir kan ?")
inputan = str(input("masukan jawaban anda = "))
if inputan == "alma":
    for i in range(1, 101):
        print(f"{i}  Ngapain?,Pacar gw itu")
else:
    print(f"bagus, fikirkan saja {inputan}")