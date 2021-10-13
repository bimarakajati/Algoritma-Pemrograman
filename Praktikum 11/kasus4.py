# Bima Rakajati
# A11.2020.13088
# 4214
# Kasus 4 - Nested Function

def penjumlahan(a):
    def jumlahkan(b):
        return a+b
    return jumlahkan

def pengurangan(a):
    def kurangkan(b):
        return a-b
    return kurangkan

def perkalian(a):
    def kalikan(b):
        return a*b
    return kalikan

def pembagian(a):
    def bagikan(b):
        return a/b
    return bagikan

def perpangkatan(a):
    def pangkatkan(b):
        return a**b
    return pangkatkan

def main():
    tambah = penjumlahan(6); print(tambah(4))
    kurang = pengurangan(10); print(kurang(5))
    kali = perkalian(5); print(kali(10))
    bagi = pembagian(10); print(bagi(2))
    pangkat = perpangkatan(5); print(pangkat(2))

if __name__ == '__main__':
    main()