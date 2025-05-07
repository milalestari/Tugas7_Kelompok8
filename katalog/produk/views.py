from django.shortcuts import render

def homepage(request):
    return render(request, 'produk/homepage.html')

def daftar_produk(request):
    produk_list = [
        {'id': 1, 'nama': 'Kemeja Batik'},
        {'id': 2, 'nama': 'Topi Rajut'},
        {'id': 3, 'nama': 'Tas Tenun'}
    ]
    return render(request, 'produk/daftar_produk.html', {'produk_list': produk_list})

def detail_produk(request, id):
    produk_data = {
        1: 'Kemeja Batik',
        2: 'Topi Rajut',
        3: 'Tas Tenun'
    }
    nama_produk = produk_data.get(id, 'Produk tidak ditemukan')
    return render(request, 'produk/detail_produk.html', {'nama_produk': nama_produk, 'id': id})

def kontak(request):
    return render(request, 'produk/kontak.html')
