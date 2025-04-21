# tugas 2. membuat perulangan untuk menampilkan deret bilangan genap berjumlah 10 deret

jumlah = int(input("masukan jumlah deret: "))
count = 0 # sebagai penghitung manual, supaya kita tau kapan perulangan berhenti
angka = 2  # mulai dari 2, karena bilangan genap pertama

while count < jumlah: # supaya kita batas akhirnya 
    print(angka, end=' ') # menampilkan bilangan genap satu dalam satu baris, di spasi mknya di truh (end='')
    angka += 2 #  menambahkan angka 2 agar angka berikutnya tetap genap 2,4,6 dst
    count += 1 # menambahkan jumlah count untuk melacak sudah brp bilangan genap yg di tampilkan