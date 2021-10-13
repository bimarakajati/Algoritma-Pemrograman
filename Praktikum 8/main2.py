# Program Rekursif
# Nama        : Bima Rakajati
# NIM         : A11.2020.13088
# Kelompok    : 4214
import pustaka

def main():
    a=int(input('Masukkan bilangan A: '))
    b=int(input('Masukkan bilangan B: '))
    print(f'{a} + {b} =',pustaka.jumlah(a,b))
    print(f'{a} - {b} =',pustaka.kurang(a,b))
    print(f'{a} * {b} =',pustaka.kali(a,b))
    print(f'{a}^{b} =',pustaka.pangkat(a,b))
    print(f'{a}! =',pustaka.faktorial(a))
    print(f'{b}! =',pustaka.faktorial(b))

if __name__ == '__main__':
    main()