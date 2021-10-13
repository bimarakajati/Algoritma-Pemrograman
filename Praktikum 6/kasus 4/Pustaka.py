def foo1(k,n,A):
    found = False
    for i in range(n):
        print('langkah ke-',i)
        if A[i] == k:
            found = True
    return found

def foo2(k,n,A):
    found = False
    templast = A[n-1]
    A[n-1] = k
    i = 0

    while A[i] != k:
        print('langkah ke-',i)
        i = i+1
    A[n-1] = templast
    if i < n-1 or k == A[n-1]:
        found = True
    return found

def foo3(k,n,A):
    # Kamus Lokal
    found = False
    i = 0
    # Algoritma
    while A[i] < k and not found:
        print("langkah ke-",i)
        if i == n-1:
            break
        i=i+1
    if A[i] == k:
        found = True
    return found

def foo4(k,n,A):
 # Kamus Lokal
 for i in range(n):
    print("langkah ke-",i)
    if A[i] == k:
        return True
    if A[i] > k:
        return False
 return False

def foo5(k,n,A):
    # Kamus Lokal
    found = False
    i = 0
    # Algoritma
    if A[0] > k or A[n-1] < k:
        found = False
    else:
        while A[i] < k and not found:
            print("langkah ke-",i)
            if i == n-1:
                break
            i=i+1
        if A[i] == k:
            found = True
    return found