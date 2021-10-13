class AkunBank(object):
    'Sistem akun bank sederhana'
    def __init__(self,nama,norek,saldo=0):
        # deklarasi atribut data,
        # perhatikan bahwa saldo memiliki nilai default 0
        self.nama = nama
        self.norek = norek
        self.saldo = saldo

    def LihatSaldo(self):
        # 1. Cetak nama dengan print
        # 2. Cetak No rek dengan print
        # 3. Cetak saldo yang ada dengan print
        # jangan lupa panggil referensi saldo dengan didahului self.
        # MULAI (1 sampai 3 baris)
        print(self.nama)
        print(self.norek)
        print(self.saldo)
        # SELESAI

    def Menabung(self,uang):
        # MULAI (1 baris)
        if (self.saldo + uang) > 0:
            self.saldo = self.saldo + uang
            print('TRANSAKSI ANDA BERHASIL DILAKSANAKAN')
        else:
            print('TRANSAKSI ANDA DITOLAK KARENA:')
            print('MINIMAL SETOR 1 RUPIAH')
        # SELESAI

    def Mengambil(self,uang):
        # MULAI (1 baris)
        if (self.saldo - uang) > 0:
            self.saldo = self.saldo-uang
            print('TRANSAKSI ANDA BERHASIL DILAKSANAKAN')
        else:
            print('TRANSAKSI ANDA DITOLAK KARENA:')
            print('SALDO TIDAK MENCUKUPI')
        # SELESAI