tinggi = int(input('Masukkan tinggi piramida yang  anda inginkan:'))

for i in range(1, tinggi+1):
    
    print((tinggi - i) * ' ' + (2 * i - 1) * '*')
