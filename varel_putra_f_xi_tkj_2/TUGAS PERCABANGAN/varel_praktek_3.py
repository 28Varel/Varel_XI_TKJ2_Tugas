#Nama : Varel Putra F
#Kelas : XI TKJ 2
#Absen : 28
#Soal : Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya.

nama_file = input ("Masukkan nama file")
daftar_file_di_server = ["varel", "putra", "firman", "syah"]

if nama_file in daftar_file_di_server:
    print("File sudah ada")
else:
    print("File belum ada")