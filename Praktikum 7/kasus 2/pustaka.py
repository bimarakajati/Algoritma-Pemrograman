def BinarySearch(A,cari):
    found = False
    batasbawah = 0 # left
    batasatas = len(A)-1 # right
    # i = 0

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
        # i=i+1
    # print('jumlah loop',i)
    return found

def InsertionSortA(n,A):
    temp = 0
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j>=0 and temp < A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = temp
    return A