from Enkapsulasi import *

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