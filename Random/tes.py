# tes = lambda a,b:a if a > b else b
# a = 5
# b = 10
# print(tes(a, b))

def xxx(a):
    def xxx(b):
        return a % b
    return xxx

tahun = [
    1992, 1994, 1996, 1998, 2000,
    2003, 2014
    ]
for i in tahun:
    xxxi = xxx(i)
    if (xxxi(4) == 0):
        print(i)

# pangkat = lambda a,b,c: a**b**c
# a = 2
# b = 3
# c = 2
# print(pangkat(a, b, c))