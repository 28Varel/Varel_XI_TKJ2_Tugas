# Nama      : Varel Putra F
# kelas     : XI TKJ 2
# No. Absen : 28
# Soal      : Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukan apakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, program harus mencetak "Sistem perlu di-restart." Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."

informasi = input("Apakah pembaruan mengharuskan restart? (perlu/tidak) : ")

if informasi == "perlu":
    print("Sistem perlu di restart!")
elif informasi == "tidak":
    print("Sistem tidak perlu direstart!")
else:
    print("Input tidak valid!!")