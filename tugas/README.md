# Pertemuan 06 — Nested Loop Python

**Nama:** Naura Palisa Ilevani
**NIM:** 2225250153
**Kelas:** 3F

## 1. Tujuan

Mempelajari nested loop, pembentukan pola, akumulasi, dan pencacahan menggunakan Python di VS Code.

## 2. Daftar Program

1. `latihan/01_pasangan_indeks.py` — menampilkan pasangan indeks dan menghitung banyak pasangan.
2. `latihan/02_pola_segitiga.py` — membuat pola segitiga menggunakan bintang.
3. `latihan/03_jumlah_per_baris.py` — menghitung jumlah perkalian pada setiap baris.
4. `latihan/04_hitung_pasangan.py` — menghitung pasangan yang memenuhi kondisi.
5. `tugas/tabel_perkalian_dan_statistik.py` — membuat tabel perkalian dan menghitung statistiknya.

## 3. Cara Menjalankan

Jalankan perintah berikut melalui terminal VS Code:

```bash
python latihan/01_pasangan_indeks.py
python latihan/02_pola_segitiga.py
python latihan/03_jumlah_per_baris.py
python latihan/04_hitung_pasangan.py
python tugas/tabel_perkalian_dan_statistik.py
```

## 4. Algoritma Tugas 3

Program meminta input bilangan bulat positif `n`. Jika `n` kurang dari atau sama dengan nol, program meminta input kembali menggunakan `while`.

Setelah input valid, program menginisialisasi `total_semua` dan `count_genap` dengan nilai nol. Loop luar menggunakan variabel `i` untuk menentukan baris, sedangkan loop dalam menggunakan variabel `j` untuk menentukan kolom.

Pada setiap pasangan, program menghitung `hasil = i * j`. Nilai tersebut ditambahkan ke `total_baris` dan `total_semua`. Jika hasil perkalian genap, `count_genap` bertambah satu. Setelah loop dalam selesai, program menampilkan jumlah baris. Setelah seluruh loop selesai, program menampilkan total keseluruhan dan banyak hasil genap.

## 5. Hasil Pengujian Tugas 3

| Input n | Total yang diharapkan | Banyak hasil genap yang diharapkan | Status              |
| ------- | --------------------: | ---------------------------------: | ------------------- |
| 1       |                     1 |                                  0 | [Isi setelah diuji] |
| 2       |                     9 |                                  3 | [Isi setelah diuji] |
| 3       |                    36 |                                  5 | [Isi setelah diuji] |

## 6. Analisis Efisiensi

Untuk input `n`, loop luar berjalan sebanyak `n` kali dan loop dalam berjalan sebanyak `n` kali untuk setiap iterasi loop luar. Oleh karena itu, perhitungan perkalian dilakukan sebanyak `n × n` kali atau `n²` kali.

## 7. Refleksi

Hal yang perlu diperhatikan dalam nested loop adalah indentasi dan lokasi inisialisasi variabel. `total_baris` harus direset setiap awal baris, sedangkan `total_semua` dan `count_genap` harus tetap terakumulasi sampai seluruh tabel selesai diproses.

Saya perlu memastikan bahwa batas perulangan, kondisi pencacahan, dan hasil pengujian sudah benar sebelum mengunggah program ke GitHub.

## 8. Sumber dan Bantuan

Sumber utama: Materi Pertemuan 06 — Nested Loop, Pola, Akumulasi, dan Pencacahan dalam Python di VS Code dan Pengumpulan melalui GitHub.

Bantuan yang digunakan: [Cantumkan bantuan atau sumber tambahan yang benar-benar digunakan].
