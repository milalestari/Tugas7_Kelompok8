# Tugas7\_Kelompok8

## 👥 Anggota Kelompok

* **Mila Lestari** - NPM 2208107010002
* **Pryta Rosela** - NPM 2208107010046
* **Widya Nurul Sukma** - NPM 2208107010054

Aplikasi katalog produk sederhana berbasis web yang dikembangkan menggunakan framework Django. Proyek ini merupakan bagian dari tugas kelompok dalam mata kuliah Pemrograman Berbasis Platform.

## 📝 Deskripsi Proyek

Aplikasi ini menyediakan fitur dasar untuk menampilkan katalog produk secara statis. Tujuan utamanya adalah memahami struktur dasar proyek Django, termasuk penggunaan views, templates, dan routing.

## 🔧 Fitur Utama

* **Beranda**: Halaman utama yang menyambut pengguna dan menyediakan navigasi ke halaman lain.
* **Daftar Produk**: Menampilkan list produk dengan informasi singkat.
* **Detail Produk**: Menampilkan informasi detail dari produk yang dipilih.
* **Kontak**: Halaman berisi informasi kontak pengembang atau pemilik toko.([Gapura Hoster][1])

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman**: Python 3.11
* **Framework**: Django 5.x
* **Basis Data**: SQLite3 (default Django)
* **Template Engine**: Django Templates([readme.so][2])

## 📁 Struktur Proyek

```
Tugas7_Kelompok8/
├── env/                 # Virtual environment (tidak perlu diunggah ke repositori)
├── katalog/             # Direktori utama proyek Django
│   ├── katalog/         # Konfigurasi proyek (settings.py, urls.py, wsgi.py, asgi.py)
│   ├── db.sqlite3       # Basis data SQLite
│   └── manage.py        # Skrip manajemen Django
└── produk/              # Aplikasi Django 'produk'
    ├── migrations/      # File migrasi basis data
    ├── templates/       # Template HTML
    │   └── produk/      # Template untuk setiap view (homepage, daftar, detail, kontak)
    ├── models.py        # Model data (saat ini kosong)
    ├── views.py         # Logika tampilan (views)
    ├── urls.py          # Routing untuk aplikasi produk
    └── ...
```



## ⚙️ Instalasi dan Persiapan

1. **Clone** repositori:

   ```bash
   git clone https://github.com/milalestari/Tugas7_Kelompok8.git
   cd Tugas7_Kelompok8/katalog
   ```



2. **Buat** dan **aktifkan** virtual environment:

   * **Linux/MacOS**:

     ```bash
     python -m venv env
     source env/bin/activate
     ```
   * **Windows**:

     ```bash
     python -m venv env
     env\\Scripts\\activate
     ```

3. **Install** Django:

   ```bash
   pip install django
   ```



4. **Jalankan** migrasi basis data:

   ```bash
   python manage.py migrate
   ```



## 🚀 Menjalankan Aplikasi

```bash
python manage.py runserver
```


Akses aplikasi melalui browser di alamat: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
