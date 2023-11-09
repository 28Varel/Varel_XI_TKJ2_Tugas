#Nama : Varel Putra F
#Kelas : XI TKJ 2
#Absen : 28
#Soal : Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium).

total_belanja = float(input("Masukan total belanjaan anda : "))
status_keanggotaan = input("Masukan Status keanggotaan anda : ")

if status_keanggotaan == "premium":
    if total_belanja > 500000:
        diskon = total_belanja * 0.15
    else:
        diskon = total_belanja * 0.10
elif status_keanggotaan == "biasa":
    if total_belanja > 300000:
        diskon = total_belanja * 0.07
    else:
        diskon = total_belanja * 0

total_belanja_setelah_diskon = total_belanja - diskon
print("total belanja anda : ", total_belanja_setelah_diskon)