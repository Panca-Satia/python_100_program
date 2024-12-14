# Login
# created by panca
# 6-11-2024

print('\n')
print('='*30)
print('Login')
print('='*30)

USERNAME = "pancasatianugraha@gmail.com"
PASSWORD = "101124yZ"

username = input('Masukan username : ')
password = input('Masukan pasword  : ')

if username != USERNAME and password == PASSWORD :
    print('Username tidak tersedia\n')
elif username == USERNAME and password != PASSWORD:
    print('Password salah\n')
else :
    print('Login berhasil\n')