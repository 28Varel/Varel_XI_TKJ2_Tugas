#Nama           : Varel Putra F
#Kelas          : XI TKJ 2
#Nomor Absen    : 28
#Soal           : Buatlah program yang menghitung berapa kali pembelahan bakteri terjadi dalam rentang waktu 2 jam.

rentang_waktu = 120
waktu_pembelahan= 20
jumlah_pembelahan = 0

while waktu_pembelahan <= rentang_waktu:
    rentang_waktu -= waktu_pembelahan
    jumlah_pembelahan += 1
    print(f'Bakteri melakukan penjumlahan sebanyak {jumlah_pembelahan} pada sisa {rentang_waktu} menit')
print(f'Dalam rentang waktu 2 jam, bakteri akan mengalami pembelahan sebanyak {jumlah_pembelahan} kali.')