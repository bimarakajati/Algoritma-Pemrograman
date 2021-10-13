def jumlah(a,b):
    if b == 0:
        return a
    elif a<0 or b<0:
        return 1 + jumlah(a,b+1)
    else:
        return jumlah(a,b-1)+1

def kurang(a,b):
    if b == 0:
        return a
    elif a<0 or b<0:
        return 1 + kurang(a,b+1)
    else:
        return kurang(a,b-1)-1

def kali(a,b):
    i = b
    result = 0
    while i>0:
        result = result + a
        i = i-1
    return result

def pangkat(a,b):
    if b == 0:
        return 1
    else:
        return a*pangkat(a,b-1)

def faktorial(n):
    if n == 1:
        return 1
    else:
        return n*faktorial(n-1)