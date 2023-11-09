# Nama      : Varel Putra F
# kelas     : XI TKJ 2
# No. Absen : 28
# Soal      : Buat progam Python yang mengambil durasi pemimjam buku dalam hari dan menentukan jenis pinjaman

durasi_pinjaman = int(input("Masukan durasi pinjaman anda (dalam hari): "))

if durasi_pinjaman <= 7:
    print("Pinjaman Pendek")
elif durasi_pinjaman > 7 <= 30:
    print("Pinjaman Menengah")
elif durasi_pinjaman >30:
    print("Pinjaman Panjang")