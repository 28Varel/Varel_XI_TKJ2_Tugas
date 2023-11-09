#Nama           : Varel Putra F
#Kelas          : XI TKJ 2
#Nomor Absen    : 28
#Soal           : membutuhkan waktu berapa bulan agar pertumbuhan ayam dari jumlah awal 100 menjadi 200 ayam dengan pertumbuhan 5%/bulan

jumlah_awal_ayam = 100
target_akhir_ayam = 200
bulan = 0

while jumlah_awal_ayam <= target_akhir_ayam:
    bulan += 1
    pertambahan_ayam = jumlah_awal_ayam * 0.05
    jumlah_awal_ayam += pertambahan_ayam
    print(f'pertumbuhan ayam {jumlah_awal_ayam} pada bulan ke {bulan}')

print(f'Dibutuhkan {bulan} bulan agar jumlah ayam melebihi {target_akhir_ayam} ekor.')