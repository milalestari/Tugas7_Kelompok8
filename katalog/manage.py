#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Baris ini digunakan di sistem UNIX agar file bisa dijalankan langsung sebagai skrip

import os  # Mengimpor modul os untuk mengatur variabel lingkungan
import sys  # Mengimpor modul sys untuk mengakses argumen baris perintah


def main():
    """Run administrative tasks."""
    # Menetapkan pengaturan default Django ke modul 'katalog.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'katalog.settings')
    try:
        # Mengimpor fungsi untuk menjalankan perintah manajemen Django dari command line
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Menangani kesalahan jika Django tidak terinstal atau tidak dapat diimpor
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Menjalankan perintah manajemen (seperti runserver, migrate, dll.)
    execute_from_command_line(sys.argv)


# Menjalankan fungsi main() jika file ini dijalankan sebagai skrip utama
if __name__ == '__main__':
    main()
