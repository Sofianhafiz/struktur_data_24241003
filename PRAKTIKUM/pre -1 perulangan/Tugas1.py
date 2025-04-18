# tugas 1. membuat bintang ganjil pada while_loop

baris = 1  # mulai dari 1 karna kita ingin mencetak bintang dari bukan 0
while baris <= 5:  # artinya kita mau mencetak bintang/pola sampai 5 baris
    bintang = "*" * (2 * baris - 1) # bagian ini adalah kunci utama untuk menghasilkan angka ganjil
    print(bintang) # untuk mencetak garisan bintang yg udah di hitung jumlahnya tdi
    baris += 1  # naik kebaris berikutnya, biar while bisa jalan terus sampai baris 5 

