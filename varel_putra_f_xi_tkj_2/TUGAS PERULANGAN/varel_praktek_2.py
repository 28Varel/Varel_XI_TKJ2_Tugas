#Nama           : Varel Putra F
#Kelas          : XI TKJ 2
#Nomor Absen    : 28
#Soal           :minggunya. Buatlah program yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10 kilometer.

jarak_awal = 5
jarak_target = 10
minggu = 0

while jarak_awal < jarak_target:
    jarak_awal = jarak_awal + 0.10 * jarak_awal
    minggu += 1
    print(f'jarak {jarak_awal} kilometar pada minggu ke {minggu}')

print(f'Dibutuhkan {minggu} minggu unutk pelari mencapailebih dari 10 kilometer')