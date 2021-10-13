import Pustaka

def main():
    # a=[12,15,20,50,100]
    # p=len(a)
    # print('a =', a)
    # c=int(input('data yg ingin dicari: '))
    # print(c, 'pada a =', Pustaka.LinearSearchSentinel(c,p,a))
    A=[12,15,20,50,100]
    # A = list(map(int,input().split()))
    print('A =', A)
    k=int(input('data yg ingin dicari: '))
    print('---foo1---')
    print(Pustaka.foo1(k,len(A),A))
    print('---foo2---')
    print(Pustaka.foo2(k,len(A),A))
    print('---foo3---')
    print(Pustaka.foo3(k,len(A),A))
    print('---foo4---')
    print(Pustaka.foo4(k,len(A),A))
    print('---foo5---')
    print(Pustaka.foo5(k,len(A),A))

if __name__ == '__main__':
    main()