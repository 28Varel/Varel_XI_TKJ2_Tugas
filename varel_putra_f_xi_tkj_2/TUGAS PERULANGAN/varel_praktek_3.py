#Nama           : Varel Putra F
#Kelas          : XI TKJ 2
#Nomor Absen    : 28
#Soal           : Buatlah progam yang menghitung berapa tahun yang dibutuhkan agar investasi melebihi 20.000 dollar

awal_investasi = 10000
investasi_target  = 20000
tahun = 0

while awal_investasi < investasi_target:
    awal_investasi = awal_investasi + 0.06 * awal_investasi
    tahun += 1
    print(f'Nilai investasi {awal_investasi} pada tahun ke {tahun}')

print(f'Dibutuhkan {tahun} tahun agar nilai investasi mencapai 20.000 dollar')