# Bima Rakajati
# A11.2020.13088
# 4214

# Kasus 1 - List Comprehension

def GetGenapList(L):
    newL = [x for x in L if x % 2 == 0]
    # n = len(L)
    # newL = []
    # for i in range(n):
    #     if L[i] % 2 == 0:
    #         newL.append(L[i])
    return newL

def main():
    L = list(map(int, input().split(' ')))
    print(GetGenapList(L))

if __name__ == '__main__':
    main()