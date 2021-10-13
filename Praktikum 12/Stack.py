class Stack(object):
    'Class yang merepresentasikan stack'
    def __init__(self,elem=[]):
        # inisialisasi langsung dengan list, bisa list kosong
        # elememen di isi dengan nilai default list kosong
        self.elem = elem

    def push(self,data):
        # isi elemen list dengan append
        # MULAI 1 baris kode
        self.elem.append(data)
        # BERHENTI

    def pop(self):
        # ambil elemen yang terakhir di push dengan pop
        # pastikan bahwa panjang elemen lebih dari 1, jika tidak
        # cetak dengan print("tidak bisa melakukan pop")
        # anda mungkin akan membutuhkan fungsi len untuk
        # mengetahui panjang elemen
        # MULAI 1 sampai 4 baris kode
        if len(self.elem) >= 1:
            self.elem.pop()
        else:
            print('tidak bisa melakukan pop')
        # BERHENTI

    def __str__(self):
        sHasil= "->"
        return ("Bawah:"+sHasil.join(map(str,self.elem))+":Atas")