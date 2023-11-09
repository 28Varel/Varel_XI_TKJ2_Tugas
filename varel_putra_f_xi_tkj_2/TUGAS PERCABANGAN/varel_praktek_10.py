# Nama      : Varel Putra F
# kelas     : XI TKJ 2
# No. Absen : 28
# Soal      : Buat progam python yang mengabil nilai performa dari karyawan dan menghitung bonus

nilai_performa = float(input("Masukan nilai performa karyawan (1-5) : "))

if nilai_performa == 1:
    print("Tidak ada bonus")
elif nilai_performa == 2:
    print("Bonus 2% dari gaji tahunan")
elif nilai_performa == 3:
    print("Bonus 5% dari gaji tahunan")
elif nilai_performa == 4:
    print("Bonus 10% dari gaji tahunan")
elif nilai_performa == 5:
    print("Bonus 20% dari gaji tahunan")
else:
    print("Input tidak valdi!")