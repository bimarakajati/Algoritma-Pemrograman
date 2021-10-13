def SequentialSearch(A,cari):
    found = False
    n = len(A)
    for i in range(n):
        if A[i] == cari:
            found = True
    # print('jumlah loop', i)
    return found

def SequentialSearchM(A,cari):
    found = False
    n = len(A)
    i = 0
    for i in range(n):
        if A[i] == cari:
            found = True
            break
    # print('jumlah loop', i)
    if found == True:
        print(found)
        return i
    else:
        return -1

def SequentialSearchM2(A,cari):
    idx = []
    found = False
    n = len(A)
    i = 0
    for i in range(n):
        if A[i] == cari:
            found = True
            idx.append(i)
            # break
    # print('jumlah loop', i)
    if found == True:
        print(cari, 'pada a, terdapat pada index ', end='')
        for i in range(len(idx)):
            print(idx[i], end=' ')
        print(', countnya adalah', len(idx))
        # return i
    else:
        print('tidak terdapat', cari, 'pada a')
        # return -1