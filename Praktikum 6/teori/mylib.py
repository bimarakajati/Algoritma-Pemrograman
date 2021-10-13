def LinearSearch(k,n,A):
    found = False

    for i in range(n):
        if A[i] == k:
            found = True
    print('jumlah loop', i)
    return found

def LinearSearchSentinel(k,n,A):
    # a=[27,5,2,10,33,500,7,49]
    found = False
    templast = A[n-1] # templast = 49
    A[n-1] = k # a=[27,5,2,10,33,500,7,k]
    i = 0

    while A[i] != k:
        i=i+1
    A[n-1] = templast # a=[27,5,2,10,33,500,7,49]
    print('jumlah loop', i)
    if i < n-1 or k == A[n-1]:
        found = True
    return found

def LinearSearchSortedSimple(k,n,A):
    found = False

    for i in range(n):
        if A[i] == k:
            found = True
        if A[i] > k:
            # found = False
            break
    print('jumlah loop', i)
    return found

def BinarySearch(k,n,A):
    found = False
    batasbawah = 0 # left
    batasatas = len(A)-1 # right
    i = 0

    # Algoritma
    while batasbawah <= batasatas and not found:
        mid = (batasatas+batasbawah)//2 # middle
        if A[mid] == k:
            found = True
        else:
            if A[mid] > k:
                batasatas = mid-1
            else:
                batasbawah = mid+1
        i=i+1
    print('jumlah loop',i)
    return found