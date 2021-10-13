# Bima Rakajati
# A11.2020.13088
# 4214

# Kasus 2 - Anonymous

def GetNama(nm):
    print(nm)

def getNim(nim):
    return nim

def main():
    GetNama('bima') # fungsi sebagai prosedur/fungsi no return/fungsi void
    nim = getNim('A11.2020.13088') # fungsi ditampung/assign pada variabel
    print(nim)
    print(getNim('A11.2020.13088')) # fungsi langsung dipanggil pada fungsi lain
    nama = lambda nm:print(nm) # pembuatan fungsi anonim (prosedur)
    nama('bima') # karena di dalam fungsi anonim tidak ada return diperlakukan seperti prosedur
    nim = lambda nim:nim # pembuatan fungsi anonim
    print(nim('A11.2020.13088')) # fungsi anonim langsung dipanggil pada fungsi lain
    nimKu = nim('A11.2020.13088') # fungsi anonim yang ditampung pada variabel
    print(nimKu)

if __name__ == '__main__':
    main()