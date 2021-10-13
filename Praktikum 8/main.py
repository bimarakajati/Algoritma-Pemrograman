# dibuat oleh:
# Nama        : Bima Rakajati
# NIM         : A11.2020.13088
# Kelompok    : 4214
import pustaka

def main():
    a=int(input('Masukkan bilangan A: '))
    b=int(input('Masukkan bilangan B: '))
    print('A + B =',pustaka.jumlah(a,b))
    print('A - B =',pustaka.kurang(a,b))
    print('A * B =',pustaka.kali(a,b))
    print('A^B =',pustaka.pangkat(a,b))
    print('A! =',pustaka.faktorial(a))
    print('B! =',pustaka.faktorial(b))

if __name__ == '__main__':
    main()