# Nama      : Varel Putra F
# kelas     : XI TKJ 2
# No. Absen : 28
# Soal      : Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori produk berdasarkan penjualan:

penjualan_produk = int(input("Masukan jumlah penjualan bulanan anda : "))

if penjualan_produk > 1000:
    kategori = "Produk Terlaris!"
elif penjualan_produk > 500 < 1000:
    kategori = "Produk Populer!"
elif penjualan_produk < 500:
    kategori = "Produk Biasa!"

print("Produk penjualan anda di kategorikan :", kategori)