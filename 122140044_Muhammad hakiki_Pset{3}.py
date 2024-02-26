file = open('Me.txt', 'w')

file.write('Nama : Muhammad Hakiki')
file.write('\nNIM : 122140044')
file.write('\nResolusi saya tahun ini: menyempurnakan skil codingan saya')

file.close()

baca_file = open('Me.txt', 'r')
print(baca_file.read())


# catatan saya
# w = write mode/ buat nulis dan bisa juga nimpah
# r = read only/ buat baca 
# a = appending mode/ nambah data di akhir baris
# r+ = baca dan nulis