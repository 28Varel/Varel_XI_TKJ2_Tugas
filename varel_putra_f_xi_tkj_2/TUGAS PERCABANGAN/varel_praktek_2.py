#Nama : Varel Putra F
#Kelas : XI TKJ 2
#Absen : 28
#Soal : Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.

from datetime import datetime

# Input estimasi waktu selesai dan tanggal target selesai dalam format tanggal (YYYY-MM-DD)
estimasi_selesai = input("Masukkan estimasi waktu selesai (YYYY-MM-DD): ")
tanggal_target = input("Masukkan tanggal target selesai (YYYY-MM-DD): ")

# Mengonversi input menjadi objek datetime
estimasi_selesai = datetime.strptime(estimasi_selesai, "%Y-%m-%d")
tanggal_target = datetime.strptime(tanggal_target, "%Y-%m-%d")

# Memeriksa apakah estimasi waktu selesai lebih awal atau sama dengan tanggal target
if estimasi_selesai <= tanggal_target:
    print("Tepat waktu")
else:
    print("Terlambat")