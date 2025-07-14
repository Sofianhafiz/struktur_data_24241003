# Program Mencatat Data Belanja Customer (versi tanpa for)

# 1. Input data customer
nama = input("Masukan nama customer: ")
tanggal = input("Masukan tanggal belanja (YYYY-MM-DD): ")
data_customer = (nama, tanggal)  # Simpan dalam tuple

# 2. Input jumlah barang
jumlah_barang = int(input("Masukan jumlah barang: "))

# 3 & 4. Input data tiap barang dan simpan dalam list of dictionaries
daftar_belanja = []

i = 0
while i < jumlah_barang:
    print(f"\nData barang ke-{i+1}:")
    nama_barang = input("Nama barang: ")
    harga = float(input("Harga satuan: "))
    qty = int(input("Jumlah beli: "))

    barang = {
        "nama": nama_barang,
        "harga": harga,
        "qty": qty
    }
    daftar_belanja.append(barang)
    i += 1

# 5. Tampilkan data dan total
print("\n=== Data Customer ===") #SENGAJA NAMBAHIN INI,BIAR ESTETIK DIKIT PAK
print(f"Nama           : {data_customer[0]}")
print(f"Tanggal Belanja: {data_customer[1]}")

print("\n=== Daftar Belanja ===")
print(f"{'No.':<5}{'Nama Barang':<20}{'Qty':<5}{'Harga':<15}{'Subtotal':<15}")
print("-" * 60)

total = 0
i = 0
while i < len(daftar_belanja):
    item = daftar_belanja[i]
    subtotal = item["harga"] * item["qty"]
    total += subtotal

    print(f"{i+1:<5}{item['nama']:<20}{item['qty']:<5}{item['harga']:,.0f}{'':<5}Rp. {subtotal:,.0f}")
    i += 1

print("-" * 60)
print(f"{'Total Belanja':<35}Rp. {total:,.0f}")
