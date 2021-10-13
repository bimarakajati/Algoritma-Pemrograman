def LinearSearchSentinel(k,n,A):
    found = False
    i = 0
    templast = A[n-1]
    A[n-1] = k
    
    while A[i] != k:
        i=i+1

    A[n-1] = templast
    if i < n-1 or k == A[n-1]:
        found = True

    return found