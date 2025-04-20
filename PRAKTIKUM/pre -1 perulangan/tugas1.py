baris = 1 # artinya kita mulai dari baris pertama karna saya pake while/ penanda kita mulai dari baris prtama
jumlah = int(input("Masukkan jumlah baris: ")) # untuk memasukan jumlah yg kita inginkan 

while baris <= jumlah: # syarat pengulangan pakai while, selama baris nilai msih kurang dri jmlah isi perulangannya
    spasi = ' ' * (jumlah - baris)         # Buat spasi kiri biar bintangnya kliatan di tengah 
    bintang = '*' * (2 * baris - 1)        # membuat Jumlah bintang ganjil di tiap baris
    print(spasi + bintang) # untuk mencetak spasi dan bintang
    baris += 1   # supaya perulangan bisa berjalan ke baris berikutnya