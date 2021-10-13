def bagi(a,b):
    if a < b: # basis
        return 0
    else: # rekurens
        return 1+bagi(a-b,b)

a = int(input('Masukkan bilangan a: '))
b = int(input('Masukkan bilangan b: '))
print('a//b =', bagi(a,b))