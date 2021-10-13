# Nama    : Bima Rakajati
# NIM     : A11.2020.13088
# Kel     : 4214

def mergesort(L): # memisahkan list mjd 2 bagian
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergesort(L[:middle])
        right = mergesort(L[middle:])
    return merge(left,right)

def merge(left,right): # menggabungkan elemen list yang telah dipisah
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1
    return result

def BinarySearch(A,cari):
    found = False
    batasbawah = 0 # left
    batasatas = len(A)-1 # right

    # Algoritma
    while batasbawah <= batasatas and not found:
        mid = (batasatas+batasbawah)//2 # middle
        if A[mid] == cari:
            found = True
        else:
            if A[mid] > cari:
                batasatas = mid-1
            else:
                batasbawah = mid+1
    return found

def main():
    # Arr = [12,3,12,3,4]
    # print(mergesort(Arr))
    A = []
    opsi = 1
    while opsi != 4:
        print('''
        ---Menu---
        1. Input List
        2. Urutkan Elemen List
        3. Cari Elemen
        4. Keluar
        ''')
        opsi = int(input('Opsi yang dipilih: '))
        if opsi == 1:
            p = int(input('Masukkan panjang list: '))
            for i in range(p):
                print(f'Masukkan elemen ke-{i+1}', end=': ')
                x = int(input())
                A.append(x)
            print('List A =', A)
        elif opsi == 2:
            if len(A) >= 2:
                A = mergesort(A)
                print('List sudah terurut', A)
            else:
                print('List masih kosong')
        elif opsi == 3:
            if len(A) >= 1:
                cari = int(input('Elemen yang ingin dicari: '))
                if len(A) >= 2:
                    A = mergesort(A)
                    print(BinarySearch(A,cari))
                elif len(A) == 1:
                    print(BinarySearch(A,cari))
            else:
                print('List masih kosong')
        else:
            break

    # print(mergesort(A))

main()