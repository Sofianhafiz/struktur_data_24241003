#  tugas 3. # membuat perulangan pada fibonacci

jumlah = int(input("Masukkan jumlah deret Fibonacci: "))

# Dua angka pertama
a = 0 
b = 1
# deret fibonacci selalu di mulai dari 0 dan 1, jadi kita tetapkan a=0 dan b=1, a = angka pertama dan b= angka ke2

count = 0 # count di gunakan untuk menghitung berapa bnyk angka yg di tampilkan, krna kita pake while

while count < jumlah: # untuk mngulangi sampai jumlah tercapai 
    print(a, end=' ') # untuk mencetak angka
    # Hitung angka berikutnya
    c = a + b
    # Geser nilai untuk lanjut ke perhitungan berikutnya
    a = b
    b = c
    count += 1 # untuk menambah jumlah angka yg sudah di tampilkan 