def SequentialSearch(A,cari):
    found = False
    n = len(A)
    for i in range(n):
        if A[i] == cari:
            found = True
    # print('jumlah loop', i)
    return found