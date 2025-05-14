# Mengimpor fungsi render dari Django untuk merender template HTML
from django.shortcuts import render

# Fungsi view untuk halaman beranda/homepage
def homepage(request):
    # Merender template 'homepage.html' di dalam folder 'produk'
    return render(request, 'produk/homepage.html')

# Fungsi view untuk menampilkan daftar produk
def daftar_produk(request):
    # Daftar produk statis yang disimpan dalam bentuk list of dictionaries
    produk_list = [
        {'id': 1, 'nama': 'Kemeja Batik'},
        {'id': 2, 'nama': 'Topi Rajut'},
        {'id': 3, 'nama': 'Tas Tenun'}
    ]
    # Merender template 'daftar_produk.html' dan mengirimkan produk_list ke template
    return render(request, 'produk/daftar_produk.html', {'produk_list': produk_list})

# Fungsi view untuk menampilkan detail suatu produk berdasarkan ID
def detail_produk(request, id):
    # Dictionary yang memetakan ID produk ke nama produk
    produk_data = {
        1: 'Kemeja Batik',
        2: 'Topi Rajut',
        3: 'Tas Tenun'
    }
    # Mengambil nama produk berdasarkan ID, atau menampilkan pesan jika ID tidak ditemukan
    nama_produk = produk_data.get(id, 'Produk tidak ditemukan')
    # Merender template 'detail_produk.html' dengan data nama produk dan ID
    return render(request, 'produk/detail_produk.html', {'nama_produk': nama_produk, 'id': id})

# Fungsi view untuk halaman kontak
def kontak(request):
    # Merender template 'kontak.html' di dalam folder 'produk'
    return render(request, 'produk/kontak.html')
