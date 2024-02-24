# Script python untuk menghitung permutasi dan kombinasi
# https://github.com/anon9497

# Mengimpor modul math dan itertools
import math
import itertools

# Meminta input pilihan rumus yang ingin dihitung
print("Silakan pilih rumus yang ingin dihitung:")
print("1. Permutasi")
print("2. Kombinasi")
pilih = int(input("Masukkan pilihan Anda (1/2): "))

# Menentukan rumus yang dipilih dan meminta input nilai yang dibutuhkan
if pilih == 1: # Jika memilih permutasi
    n = int(input("Masukkan nilai n: "))
    r = int(input("Masukkan nilai r: "))
    # Menghitung permutasi dengan fungsi math.perm(n, r)
    perm = math.perm(n, r)
    print("Permutasi dari", n, "objek yang diambil", r, "objek adalah", perm)
    # Menghasilkan semua kemungkinan permutasi dengan fungsi itertools.permutations(iterable, r)
    iter = range(1, n + 1) # Membuat iterable dari 1 sampai n
    perms = itertools.permutations(iter, r) # Membuat objek generator permutasi
    print("Berikut adalah semua kemungkinan permutasi:")
    for p in perms: # Loop untuk menampilkan setiap permutasi
        print(p)
elif pilih == 2: # Jika memilih kombinasi
    n = int(input("Masukkan nilai n: "))
    r = int(input("Masukkan nilai r: "))
    # Menghitung kombinasi dengan fungsi math.comb(n, r)
    comb = math.comb(n, r)
    print("Kombinasi dari", n, "objek yang diambil", r, "objek adalah", comb)
    # Menghasilkan semua kemungkinan kombinasi dengan fungsi itertools.combinations(iterable, r)
    iter = range(1, n + 1) # Membuat iterable dari 1 sampai n
    combs = itertools.combinations(iter, r) # Membuat objek generator kombinasi
    print("Berikut adalah semua kemungkinan kombinasi:")
    for c in combs: # Loop untuk menampilkan setiap kombinasi
        print(c)
else: # Jika memilih selain 1 atau 2
    print("Pilihan tidak valid!") # Menampilkan pesan kesalahan
