# Program Rekapitulasi Data Nilai Mahasiswa

# Meminta jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Inisialisasi dictionary
data_mahasiswa = {}

# Input data untuk setiap mahasiswa
for _ in range(jumlah_mahasiswa):
    print("\nMasukkan data mahasiswa:")
    nim = input("NIM   : ")
    nama = input("Nama  : ")

    jumlah_mk = int(input("Jumlah mata kuliah: "))
    mata_kuliah = []

    for i in range(jumlah_mk):
        mk = input(f"  Nama mata kuliah ke-{i+1} : ")
        nilai = float(input(f"  Nilai mata kuliah ke-{i+1}: "))
        mata_kuliah.append((mk, nilai))  # disimpan sebagai tuple

    # Simpan ke dictionary
    data_mahasiswa[nim] = {
        "nama": nama,
        "mata_kuliah": mata_kuliah
    }

# Menampilkan rata-rata nilai untuk tiap mahasiswa
print("\n--- Rata-rata Nilai Mahasiswa ---")
for nim, info in data_mahasiswa.items():
    nama = info["nama"]
    nilai_list = info["mata_kuliah"]

    total_nilai = sum(nilai for _, nilai in nilai_list)
    jumlah_nilai = len(nilai_list)
    rata_rata = total_nilai / jumlah_nilai if jumlah_nilai > 0 else 0

    print(f"\nNIM   : {nim}")
    print(f"Nama  : {nama}")
    print(f"Rata-rata nilai: {rata_rata:.2f}")

# Menampilkan seluruh data mahasiswa dengan format rapi
print("\n--- Daftar Seluruh Data Mahasiswa ---")
for i, (nim, info) in enumerate(data_mahasiswa.items(), start=1):
    print(f"{i}. NIM  : {nim}")
    print(f"   Nama : {info['nama']}")
    print("   Mata kuliah dan nilai:")
    for mk, nilai in info["mata_kuliah"]:
        print(f"     - {mk}: {nilai}")
    print()