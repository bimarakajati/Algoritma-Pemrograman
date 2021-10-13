# Bima Rakajati
# A11.2020.13088

class Kalkulator(object):
    'kalkulator PBO'
    def __init__(self,bil1,bil2):
        self.bil1 = bil1
        self.bil2 = bil2
    def addition(self):
        return (self.bil1 + self.bil2)
    def subtraction(self):
        return (self.bil1 - self.bil2)
    def multiplication(self):
        return (self.bil1 * self.bil2)
    def division(self):
        return (self.bil1 // self.bil2)
    def modulus(self):
        return (self.bil1 % self.bil2)

def main():
    jawab = 'ya'
    
    while jawab == 'ya':
        # Menu kalkulator
        print('MENU OPERASI')
        print('1. Penjumlahan')
        print('2. Pengurangan')
        print('3. Perkalian')
        print('4. Pembagian')
        print('5. Sisa Pembagian')
        
        # Input dari user
        pilihan = input('\nMasukkan pilihan(1-5): ')
        bil1 = int(input('Masukkan bilangan pertama: '))
        bil2 = int(input('Masukkan bilangan kedua: '))        
        calc = Kalkulator(bil1, bil2)
        
        if pilihan == '1': # Penjumlahan
            print("Hasil Penjumlahan =", calc.addition())
        elif pilihan == '2': # Pengurangan
            print("Hasil Pengurangan =", calc.subtraction())
        elif pilihan == '3': # Perkalian
            print("Hasil Perkalian =", calc.multiplication())
        elif pilihan == '4': # Pembagian
            print("Hasil Pembagian =", calc.division())
        elif pilihan == '5': # Modulus
            print("Hasil Sisa Pembagian =", calc.modulus())
        else: # Input salah apabila user memasukkan selain angka 1-5
            print('Input salah')

        # Agar program bisa ke menu setelah selesai melakukan operasi
        jawab = input('\nIngin kembali ke menu (ya/tidak)? ').lower()

if __name__ == "__main__":
    main()