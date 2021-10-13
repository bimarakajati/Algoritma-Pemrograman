# dibuat oleh:
# Nama        : Bima Rakajati
# NIM         : A11.2020.13088
# Kelompok    : 4214

def kali(a,b): # a = 3, b = 2
    i = b # i = 2
    result = 0
    while i>0:
        result = result + a # 0 + 3 = 3 + 3 = 6
        i = i-1 # 2 - 1 = 1 - 1 = 0
    return result
a, b = 3, 2
print('A * B =',kali(a,b))