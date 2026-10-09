# Tugas 3: Tabel Perkalian dan Statistik

print("Tabel Perkalian dan Statistik")

n = int(input("Masukkan n: "))

# Validasi agar n harus positif
while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan n: "))

# Inisialisasi total keseluruhan dan pencacahan genap
total_semua = 0
count_genap = 0

# Loop luar untuk mengatur baris
for i in range(1, n + 1):
    total_baris = 0

    # Loop dalam untuk mengatur kolom
    for j in range(1, n + 1):
        hasil = i * j

        # Menampilkan hasil perkalian
        print(f"{hasil:4}", end="")

        # Akumulasi jumlah per baris dan keseluruhan
        total_baris += hasil
        total_semua += hasil

        # Menghitung hasil perkalian yang genap
        if hasil % 2 == 0:
            count_genap += 1

    # Dijalankan setelah satu baris selesai
    print(f"   | jumlah baris = {total_baris}")

# Ringkasan setelah seluruh tabel selesai
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")