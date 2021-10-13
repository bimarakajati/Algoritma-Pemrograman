class Kalkulator(object): # class kalkulator
    'kalkulator Sederhana'
    def __init__(self,x,y): # fungsi method init = digunakan untuk konfigurasi object yang telah di-construct
        self.x = x # variabel untuk bil pertama
        self.y = y # variabel untuk bil kedua
    def Jumlah(self): # fungsi penjumlahan
        return (self.x + self.y) # mengembalikan hasil penjumlahan bil pertama dg kedua
    def Kurang(self): # fungsi pengurangan
        return (self.x - self.y)  # mengembalikan hasil pengurangan bil pertama dg kedua
    def Kali(self): # fungsi perkalian
        return (self.x * self.y)  # mengembalikan hasil perkalian bil pertama dg kedua
    def Bagi(self): # fungsi pembagian
        return (self.x // self.y)  # mengembalikan hasil pembagian bil pertama dg kedua
    def Modulus(self): # fungsi sisa bagi
        return (self.x % self.y)  # mengembalikan hasil sisa bagi bil pertama dg kedua

def main(): # program utama
    x = int(input('Masukkan bilangan pertama : ')) # input user untuk bil pertama
    y = int(input('Masukkan bilangan kedua : ')) # input user untuk bil kedua
    calc = Kalkulator(x, y) # inisialisasi variabel calc untuk memasukkan bil 1 dan 2 ke class kalkulator
    print("Hasil Penjumlahan =", calc.Jumlah()) # mencetak hasil penjumlahan
    print("Hasil Pengurangan =", calc.Kurang()) # mencetak hasil pengurangan
    print("Hasil Perkalian =", calc.Kali()) # mencetak hasil perkalian
    print("Hasil Pembagian =", calc.Bagi()) # mencetak hasil pembagian
    print("Hasil Sisa Pembagian =", calc.Modulus()) # mencetak hasil sisa bagi

if __name__ == "__main__": # apabila name sama dengan main maka akan masuk program utama
    main()