# BIMA RAKAJATI
# A11.2020.13088
# 4214

class AkunBank(object):
    'Sistem akun bank sederhana'
    def __init__(self,nama,norek,saldo=0):
        # deklarasi atribut data,
        # perhatikan bahwa saldo memiliki nilai default 0
        self.nama = nama
        self.norek = norek
        self.__saldo = saldo

    def LihatSaldo(self):
        # 1. Cetak nama dengan print
        # 2. Cetak No rek dengan print
        # 3. Cetak saldo yang ada dengan print
        # jangan lupa panggil referensi saldo dengan didahului self.
        # MULAI (1 sampai 3 baris)
        print('Nama     =', self.nama)
        print('No Rek   =', self.norek)
        print('Saldo    =', self.__saldo)
        # SELESAI

    def Menabung(self,uang):
        # MULAI (1 baris)
        if (self.__saldo + uang) > 0:
            self.__saldo = self.__saldo + uang
            print('TRANSAKSI ANDA BERHASIL DILAKSANAKAN')
        else:
            print('TRANSAKSI ANDA DITOLAK KARENA:')
            print('MINIMAL SETOR 1 RUPIAH')
        # SELESAI

    def Mengambil(self,uang):
        # MULAI (1 baris)
        if (self.__saldo - uang) > 0:
            self.__saldo = self.__saldo-uang
            print('TRANSAKSI ANDA BERHASIL DILAKSANAKAN')
        else:
            print('TRANSAKSI ANDA DITOLAK KARENA:')
            print('SALDO TIDAK MENCUKUPI')
        # SELESAI

def main():
    akunku = AkunBank('Bima Rakajati', 13088)
    akunku.LihatSaldo()
    akunku.Menabung(275000)
    akunku.LihatSaldo()
    akunku.Mengambil(25000)
    akunku.LihatSaldo()

if __name__ == "__main__":
    main()