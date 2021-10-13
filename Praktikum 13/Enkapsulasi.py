class CobaNoCons:
    'Kelas uji coba tanpa inherit dari object dan tanpa konstruktor'
    #Attribut disini dengan akses private gunakan “__”
    __cekAttrib = '' #rubah di baris ini

    #Method disini
    def setAttrib(self,varAttr):
        self.__cekAttrib = varAttr # rubah di baris ini
    def getAtrrib(self):
        return self.__cekAttrib # rubah di baris ini

def main():
    # instance mengakses pada konstruktor kosong/tidak ada konstruktor
    cObj = CobaNoCons()
    # setter method untuk mengeset suatu nilai dari
    # parameter akutual ke atrribut class
    cObj.setAttrib("Hello World!")
    # assign langsung ke atrribut akan gagal karena di private
    cObj.cekAttrib = "gagal" # rubah di baris ini
    # getter method untuk mekanisme pemanggilan attribut kelas
    print(cObj.getAtrrib())

if __name__ == '__main__':
    main()