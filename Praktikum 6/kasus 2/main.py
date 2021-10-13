import Pustaka

def main():
    # a=[5,2,10,27,10,33]
    # a=[5,2,10,27,33]
    # a=[5,5,5,6,5,5,5]
    a=[1,5,2,10,15] 
    # p=len(a)
    print('a =', a)
    c=int(input('data yg ingin dicari: '))
    print(c, 'pada a =', Pustaka.SequentialSearch(a,c))
    # print(c, 'pada a, terdapat pada index', Pustaka.SequentialSearchM(a,c))
    # print(c, 'pada a, terdapat pada index', Pustaka.SequentialSearchM2(a,c))
    # Pustaka.SequentialSearchM2(a,c)
    

if __name__ == '__main__':
    main()