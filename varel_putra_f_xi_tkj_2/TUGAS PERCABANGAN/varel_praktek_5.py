# Nama      : Varel Putra F
# kelas     : XI TKJ 2
# No. Absen : 28
# Soal      : Buat program Python yang mengambil nilai tugas (skala 0-100) dan nilai ujian (skala 0-100) seorang siswa dan menentukan nilai akhirnya. Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswa lulus dengan nilai "Lulus". Jika tidak, siswa gagal dengan nilai "Gagal".

nilai_tugas = int(input("Masukan nilai tugas anda (0-100) : "))
nilai_ujian = int(input("Masukan nilai ujian anda (0-100) : "))

if nilai_tugas > 70 and nilai_ujian > 60:
    hasil = "LULUS!!"
else:
    hasil = "GAGAL!!"

print("hasil dari nilai akhir, anda dinyatakan :", hasil)