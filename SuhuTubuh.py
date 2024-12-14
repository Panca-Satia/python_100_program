#suhu untuk manusia
# Dibuat Oleh Panca
# 8-11-2024

print('\n')
print('='*30)
print('suhu tubuh untuk manusia')
print('='*30)

while True:
 temperatur = float(input('\nmasukan suhu tubuh : '))

 if temperatur < 35 :
    print("Hipotermia")
 elif temperatur == 36 :
    print("Normal")
 elif temperatur >= 38 :
    print("Demam")
 elif temperatur <= 100 :
    print("Kamu Kenapa?")