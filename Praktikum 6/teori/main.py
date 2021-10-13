import mylib

def main():
    # a=[27,5,2,10,33,500,7,49]
    # p=len(a)
    # print('a =', a)
    # c=int(input('data yg ingin dicari: '))
    # print(c, 'pada a =', mylib.LinearSearch(c,p,a))
    # print(c, 'pada a =', mylib.LinearSearchSentinel(c,p,a))
    a=[1,5,7,10,27,33,49,500]
    p=len(a)
    print('a =', a)
    c=int(input('data yg ingin dicari: '))
    print(c, 'pada a =', mylib.LinearSearch(c,p,a))
    print(c, 'pada a =', mylib.LinearSearchSentinel(c,p,a))
    print(c, 'pada a =', mylib.LinearSearchSortedSimple(c,p,a))
    print(c, 'pada a =', mylib.BinarySearch(c,p,a))
    

if __name__ == '__main__':
    main()