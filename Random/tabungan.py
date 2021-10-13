# Program Tabungan Sederhana
# Dibuat oleh:
# Nama        : Bima Rakajati
# NIM         : A11.2020.13088
# Kelompok    : 4214

def tabung(a):
    for i in range(a):
        minggu = []
        print(f'\nTabungan bulan ke-{i+1}')
        for j in range(3):
            x = int(input(f'Masukan tabungan minggu ke-{j+1}: '))
            minggu.append(x)
        bulan.append(minggu)
    return bulan

def total(bulan):
    result = sum(map(sum, bulan))
    return result

if __name__ == '__main__':
    global bulan
    bulan = []
    while(True):
        print('''
        PROGRAM MENABUNG
        ---Menu---
        1. Input Tabungan
        2. Lihat Tabungan
        3. Total Tabungan
        4. Keluar
        ''')
        opsi = int(input('Opsi yang dipilih: '))
        if opsi == 1:
            x = int(input('Berapa bulan anda menabung? '))
            if x >= 1:
                print('\nList Tabungan =', tabung(x))
            else:
                print('\nError, harap input angka 1 keatas')

        elif opsi == 2:
            if len(bulan) >= 1:
                print(f'\nBerikut adalah tabungan anda selama {len(bulan)} bulan:')
                for x in range(len(bulan)):
                    print(f'Tabungan bulan ke-{x+1}: {bulan[x]}')
            else:
                print('\nTabungan masih kosong')
        
        elif opsi == 3:
            if len(bulan) >= 1:
                print(f'\nTotal semua tabungan anda selama {len(bulan)} bulan: {total(bulan)}')
            else:
                print('\nTabungan masih kosong')

        elif opsi == 4:
            print('\nProgram Keluar')
            break

        else:
            print('\nInput Salah')