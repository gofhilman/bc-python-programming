# Game Tebak Angka di dalam Terminal

Proyek ini bertujuan untuk membuat permainan sederhana di terminal di mana pemain harus menebak angka rahasia antara 1–100. Program akan memberi petunjuk apakah tebakan terlalu tinggi atau terlalu rendah, dan permainan berakhir jika pemain menebak dengan benar atau kehabisan percobaan.

## Tugas Pengerjaan

### 1. Persiapan

Mulailah dengan membuat sebuah file Python baru, misalnya bernama `tebak_angka.py`. Di dalam file ini, impor modul `random`, karena kita akan menggunakannya untuk menghasilkan angka rahasia secara acak.

```python
import random
```

### 2. Membuat Class Game

Selanjutnya, buat sebuah kelas bernama `NumberGuessingGame`. Kelas ini akan menjadi pusat logika permainan. Di dalam method `__init__`, tentukan batas angka minimum dan maksimum, yaitu 1 sampai 100, serta jumlah percobaan maksimal (misalnya 10). Jangan lupa memanggil method `reset_game()` agar permainan dimulai dengan kondisi baru.

### 3. Reset Game

Buat method `reset_game()` untuk mengatur ulang permainan. Di sini, angka rahasia dipilih secara acak antara 1–100, jumlah percobaan diatur kembali ke nol, dan status permainan ditandai sebagai belum selesai.

### 4. Validasi Tebakan

Tambahkan method `validate_guess(guess)` untuk memastikan bahwa tebakan pemain berada dalam rentang angka yang valid, yaitu antara 1 dan 100. Jika tebakan keluar dari rentang ini, program akan memberi tahu bahwa input tidak sah.

### 5. Mengecek Tebakan

Buat method `check_guess(guess)` untuk membandingkan tebakan dengan angka rahasia. Jika sama, hasilnya "correct". Jika lebih besar, hasilnya "high". Jika lebih kecil, hasilnya "low".

### 6. Memproses Tebakan

Buat method `make_guess(guess)` yang akan memproses tebakan pemain. Input diubah menjadi integer, lalu divalidasi. Jika valid, jumlah percobaan bertambah. Program kemudian memeriksa apakah tebakan benar, terlalu tinggi, atau terlalu rendah. Jika benar, permainan berakhir dan skor dihitung. Jika percobaan habis, permainan juga berakhir dengan pesan kekalahan. Jika belum, pemain diberi petunjuk untuk mencoba lagi.

### 7. Loop Permainan

Buat method `play()` sebagai loop utama permainan. Tampilkan pesan sambutan, minta input tebakan dari pemain, lalu tampilkan hasilnya (benar, salah, terlalu tinggi, atau terlalu rendah). Jangan lupa juga menampilkan sisa percobaan. Permainan akan terus berjalan sampai pemain menang atau kalah.

### 8. Fungsi Main

Terakhir, buat fungsi `play_game()` untuk memanggil kelas dan menjalankan permainan. Gunakan blok berikut agar permainan bisa langsung dijalankan dari terminal:

```python
if __name__ == "__main__":
    play_game()
```

## Tantangan Tambahan (Opsional)

### 1. Leaderboard

Setelah versi dasar permainan selesai, kamu bisa menambahkan fitur Leaderboard untuk membuat permainan lebih kompetitif. Di awal permainan, minta pemain untuk memasukkan nama mereka. Setelah permainan berakhir, hitung skor berdasarkan jumlah percobaan yang digunakan untuk menebak angka dengan benar, misalnya jika pemain menebak dalam satu kali percobaan, skornya adalah 10; jika dua kali, skornya 9; dan seterusnya. Skor ini kemudian disimpan dalam sebuah file, dan setelah semua pemain selesai bermain, tampilkan peringkat skor tertinggi agar semua bisa melihat siapa penebak terbaik.

### 2. Mode Komputer Menebak

Kamu juga bisa menambahkan mode Komputer Menebak, di mana peran dibalik: pemain memilih angka rahasia, dan komputer yang mencoba menebaknya. Komputer akan menggunakan strategi seperti binary search untuk mempersempit kemungkinan angka secara efisien. Setiap kali komputer memberikan tebakan, pemain harus memberi petunjuk apakah tebakan tersebut terlalu tinggi, terlalu rendah, atau sudah benar. Permainan berakhir saat komputer berhasil menebak angka yang dipilih pemain.
