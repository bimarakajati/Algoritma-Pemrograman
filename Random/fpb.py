# Program Untuk Mencari Faktor Persekutuan Terbesar (FPB)
# Dibuat oleh:
# Nama        : Bima Rakajati
# NIM         : A11.2020.13088
# Kelompok    : 4214

def fpb(x, y): # 10, 0
    # basecase: saat y sama dengan nol maka return x
    if (y == 0): 
        return x
    # rekurens: saat y belum mencapai 0, maka terjadi rekursif
    else:
        return fpb(y, x % y) # 10, 20 % 10 = 0
def main():
    # mendapatkan user input
    x = int(input('Masukkan bilangan pertama : ')) # 20
    y = int(input('Masukkan bilangan kedua : ')) # 30
    print('Faktor Persekutuan Terbesarnya adalah', fpb(x, y))
main()