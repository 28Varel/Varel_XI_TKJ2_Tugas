# Nama      : Varel Putra F
# kelas     : XI TKJ 2
# No. Absen : 28
# Soal      : Buat program Python yang mengambil total belanjaan pelanggan dan memberikan diskon

total_belanja = float(input("Total Belanjaan Anda : "))

if total_belanja > 500000:
    diskon = total_belanja * 0.10
elif total_belanja >= 300000:
    diskon = total_belanja * 0.05
else:
    diskon = 0

total_pembayaran = total_belanja - diskon
print("Total pembayaran anda adalah: ", total_pembayaran)